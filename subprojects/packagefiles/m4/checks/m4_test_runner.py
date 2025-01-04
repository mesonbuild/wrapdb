import sys
import subprocess
import os

# We want to print line endings normally, but each line should be a b'' string
def clean(x):
    lines = []
    for line in x.splitlines():
        if b'examples' in line:
            lines.append(str(line.replace(b'\\',b'/')))
        else:
            lines.append(str(line))
    return '\n'.join(lines)

def check_error(run_result,
                expected_code,
                expected_out,
                expected_err,
                ignore_err,
                m4_input,
                m4_path,
                examples_path
                ) -> int:
    res = 0
    lout = clean(run_result.stdout).replace(str(m4_path.encode())[2:-1], 'm4').replace(examples_path, 'examples').replace('m4.exe', 'm4')
    lerr = clean(run_result.stderr).replace(str(m4_path.encode())[2:-1], 'm4').replace(examples_path, 'examples').replace('m4.exe', 'm4')
    rout = clean(expected_out)
    rerr = clean(expected_err)
    if run_result.returncode != expected_code:
        print('Unexpected return code: {0}'.format(run_result.returncode))
        print('Expected return code: {0}'.format(expected_code))
        res = 1
    if lout != rout:
        print('Unexpected stdout:\n{0}'.format(lout))
        print('Expected stdout:\n{0}'.format(rout))
        res = 1
    if not ignore_err and lerr != rerr and lerr != 'Killed':
        print('Unexpected stderr:\n{0}'.format(lerr))
        print('Expected stderr:\n{0}'.format(rerr))
        res = 1
    print('The input was:\n{0}'.format(clean(m4_input)))
    return res

def main() -> int:
    m4_path = sys.argv[1]
    input_path = sys.argv[2]
    workdir = sys.argv[3]
    examples_path = workdir + '/examples'
    if ':' in examples_path:
        examples_path = examples_path.partition(':')[2]
    with open(input_path, 'rb') as input_file:
        expected_out = bytes()
        expected_err = bytes()
        ignore_err = False
        m4_input = bytes()
        for line in input_file.read().splitlines():
            if line.startswith(b'dnl @ expected status: '):
                expected_code = int(line[len('dnl @ expected status: '):].rstrip())
            if line.startswith(b'dnl @ extra options: '):
                args = line[len('dnl @ extra options: '):].rstrip().decode()
            if line.startswith(b'dnl @result{}'):
                expected_out += line[len('dnl @result{}'):] + os.linesep.encode()
            if line.startswith(b'dnl @error{}'):
                expected_err += line[len('dnl @error{}'):] + os.linesep.encode()
            if line.startswith(b'dnl @ expected error: ignore'):
                ignore_err = True
            if not line.startswith(b'dnl @'):
                m4_input += line + b'\n'
        runargs = []
        runargs.append(m4_path)
        runargs.append('-d')
        for arg in args.split(' '):
            if len(arg) > 0:
                runargs.append(arg)
        runargs.append('-')
        print('Arguments are: {0}'.format(' '.join(runargs)))
        res = subprocess.run(runargs,
                             input=m4_input,
                             capture_output=True)
        if res.returncode == 77:
            return 77
        return check_error(res, expected_code, expected_out, expected_err, ignore_err, m4_input, m4_path, examples_path.replace('\\','/'))

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
