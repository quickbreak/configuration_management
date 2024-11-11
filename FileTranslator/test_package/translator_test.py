import pytest
import translator


def test_translate_value__str():
    assert translator.translate_value('string', '') == '@"string"'


def test_translate_value__int():
    assert translator.translate_value(345, '') == 345


def test_translate_value__list():
    assert translator.translate_value([0, 1, 2], '') == '({ 0, 1, 2 })'


def test_translate_value__dict():
    res = 'dict(\n\
   @"key_1" = @"value_1"\n\
   @"key_2" = 2\n\
   @"key_3" = ({ 0, 1 })\n\
)'

    input_dict = {
        "key_1": "value_1",
        "key_2": 2,
        "key_3": [0, 1]
    }
    assert translator.translate_value(input_dict, '') == res


def test_calc_expressions__add():
    res = '@"result for ?[k1 k2 add]" = 52\n'
    expressions = ['?[k1 k2 add]']
    constants = {
        "k1": 24,
        "k2": 28
    }
    assert translator.calc_expressions(expressions, constants, '') == res


def test_calc_expressions__concatenate():
    res = '@"result for ?[k1 k2 concatenate]" = @"first line+second line"\n'
    expressions = ['?[k1 k2 concatenate]']
    constants = {
        "k1": "first line+",
        "k2": "second line"
    }
    assert translator.calc_expressions(expressions, constants, '') == res


def test_calc_expressions__max():
    res = '@"result for ?[k1 k2 max]" = 28\n'
    expressions = ['?[k1 k2 max]']
    constants = {
        "k1": 24,
        "k2": 28
    }
    assert translator.calc_expressions(expressions, constants, '') == res


def test_translate_dict():
    res = 'dict(\n\
   @"key_1" = @"value_1"\n\
   @"key_2" = 2\n\
   @"key_3" = ({ 0, 1 })\n\
)'

    input_dict = {
        "key_1": "value_1",
        "key_2": 2,
        "key_3": [0, 1]
    }
    assert translator.translate_dict(input_dict, '   ') == res


def test_translate():
    res = 'dict(\n\
   global @"constant_a" = 123\n\
   global @"constant_b" = 321\n\
   global @"constant_s1" = @"hello "\n\
   global @"constant_s2" = @"world"\n\
   @"expression_add" = @"?[constant_a constant_b add]"\n\
   @"expression_concatenate" = @"?[constant_s1 constant_s2 concatenate]"\n\
   @"expression_max" = @"?[constant_a constant_b max]"\n\
   @"list" = ({ 1, 2, 3 })\n\
   @"ordinary_line" = @"I am a line"\n\
   @"some_log_path" = @"./log/log.json"\n\
   @"dict in dict" = dict(\n\
      @"key1" = @"value1"\n\
      @"key2" = 2\n\
      @"dict in dict in dict" = dict(\n\
         @"key3" = @"value3"\n\
         global @"constant_52" = 34\n\
      )\n\
   )\n\
   @"result for ?[constant_a constant_b add]" = 444\n\
   @"result for ?[constant_s1 constant_s2 concatenate]" = @"hello world"\n\
   @"result for ?[constant_a constant_b max]" = 321\n\
)'
    assert translator.translate("./test_package/test_input.json", "./test_package/test_output.michael") == res
