import imp
import sys

sys.path.insert(1, '../')

from get import main


def test_command(capsys):
    main.main(['--object', '{"name":"John", "age":30, "city":"New York"}', '--key', 'name'])
    output = capsys.readouterr()
    result = output.out.split('\n')
    res_len = len(result)
    assert result[res_len - 2] == "Value = John"

    main.main(['--object', '{"x":{"y":{"z":"a"}}}', '--key', 'x/y/z'])
    output = capsys.readouterr()
    result = output.out.split('\n')
    res_len = len(result)
    assert result[res_len - 2] == "Value = a"

    main.main(['--object', '{"x":{"y":{"z":"a"}}}', '--key', 'x/y'])
    output = capsys.readouterr()
    result = output.out.split('\n')
    res_len = len(result)
    assert result[res_len - 2] == "Value = {'z': 'a'}"
