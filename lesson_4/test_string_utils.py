from string_utils import StringUtils
import pytest

@pytest.mark.parametrize('TestStr, ResultStr',[("test","Test"),("clone","Clone"),("start","Start")])
def test_capitilize_StringUtils(TestStr, ResultStr):
    StrIn = StringUtils()
    StrOut = StrIn.capitilize(TestStr)
    assert StrOut == ResultStr

@pytest.mark.parametrize('TestStr, ResultStr',[("        test","test"), ("clone     ","clone     ") , ("   -  start","-  start")])
def test_trim_StringUtils(TestStr, ResultStr):
    StrIn = StringUtils()
    StrOut = StrIn.trim(TestStr)
    assert StrOut == ResultStr
        


@pytest.mark.parametrize('TestStr, delimeter, Result',[("t-e-s-t","-",["t","e","s","t"]),("test","-",["test"])])
def test_to_list_StringUtils(TestStr, delimeter,  Result):
    StrIn = StringUtils()
    StrOut = StrIn.to_list(TestStr,delimeter)
    assert StrOut == Result
    

@pytest.mark.parametrize('TestStr, symbol, Result',[("test","-",False),("test","e",True)])
def test_contains_StringUtils(TestStr, symbol,  Result):
    StrIn = StringUtils()
    StrOut = StrIn.contains(TestStr,symbol)
    assert StrOut == Result
    

@pytest.mark.parametrize('TestStr, symbol, Result',[("test","es","tt"),("test","zz","test")])
def test_delete_symbol_StringUtils(TestStr, symbol,  Result):
    StrIn = StringUtils()
    StrOut = StrIn.delete_symbol(TestStr,symbol)
    assert StrOut == Result
    
@pytest.mark.parametrize('TestStr, symbol, Result',[("test","t",True),("test","e",False)])
def test_starts_with_StringUtils(TestStr, symbol,  Result):
    StrIn = StringUtils()
    StrOut = StrIn.starts_with(TestStr,symbol)
    assert StrOut == Result

@pytest.mark.parametrize('TestStr, symbol, Result',[("test","t",True),("test","e",False)])
def test_end_with_StringUtils(TestStr, symbol,  Result):
    StrIn = StringUtils()
    StrOut = StrIn.end_with(TestStr,symbol)
    assert StrOut == Result

@pytest.mark.parametrize('TestStr,  Result',[("",True),("test",False)])
def test_is_empty_StringUtils(TestStr, Result):
    StrIn = StringUtils()
    StrOut = StrIn.is_empty(TestStr)
    assert StrOut == Result



@pytest.mark.parametrize('TestStr, delimeter, Result',[(["t","e","s","t"],"-","t-e-s-t")])

def test_list_to_string_StringUtils(TestStr, delimeter,  Result):
    StrIn = StringUtils()
    StrOut = StrIn.list_to_string(TestStr,delimeter)
    assert StrOut == Result


@pytest.mark.parametrize('TestStr, delimeter, Result',[(["t","e","s","t"],"-","t-e-s-t"),(["t","e","s","t"],"-","t- e - s - t -")])
@pytest.mark.xfail
def test_xfail_list_to_string_StringUtils(TestStr, delimeter,  Result):
    StrIn = StringUtils()
    StrOut = StrIn.list_to_string(TestStr,delimeter)
    assert StrOut == Result