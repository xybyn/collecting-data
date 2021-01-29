import unittest
from utils import *
from DataProcessingPipeline import *

class UtilsTests(unittest.TestCase):

    def test_remove_remove_slash_n_should_return_white_space(self):

        #arrange
        self.pipeline = DataProcessingPipeline("\n")
        self.pipeline.add(remove_slash_n)
        #act

        result = self.pipeline.target_string

        #assert
        self.assertTrue(result == ' ')

    def test_remove_remove_slash_n_should_return_3_white_spaces(self):

        #arrange
        self.pipeline = DataProcessingPipeline("\n\n\n")
        self.pipeline.add(remove_slash_n)
        #act

        result = self.pipeline.target_string

        #assert
        self.assertTrue(result == '   ')

    def test_remove_remove_slash_n_should_return_same_string(self):
        # arrange
        self.pipeline = DataProcessingPipeline("hello")
        self.pipeline.add(remove_slash_n)
        # act

        result = self.pipeline.target_string

        # assert
        self.assertTrue(result == 'hello')

    def test_remove_td_should_return_same_string(self):
        # arrange
        self.pipeline = DataProcessingPipeline("hello")
        self.pipeline.add(remove_td)
        # act

        result = self.pipeline.target_string

        # assert
        self.assertTrue(result=="hello")

    def test_remove_td_should_return_white_space_1_bracket(self):
        # arrange
        self.pipeline = DataProcessingPipeline("<td>")
        self.pipeline.add(remove_td)
        # act

        result = self.pipeline.target_string

        # assert
        self.assertTrue(result==" ")

    def test_remove_td_should_return_2_white_spaces_2_brackets(self):
        # arrange
        self.pipeline = DataProcessingPipeline("<td></td>")
        self.pipeline.add(remove_td)
        # act

        result = self.pipeline.target_string

        # assert
        self.assertTrue(result=="  ")


    def test_remove_tags_should_return_white_space(self):
        # arrange
        self.pipeline = DataProcessingPipeline("<td>")
        self.pipeline.add(remove_td)
        # act

        result = self.pipeline.target_string

        # assert
        self.assertTrue(result==" ")

    def test_remove_tags_should_return_string_with_out_tags(self):
        # arrange
        self.pipeline = DataProcessingPipeline("<td>hello world<tds><td>")
        self.pipeline.add(remove_tags)
        # act

        result = self.pipeline.target_string

        # assert
        self.assertEqual(result," hello world  ")

    def test_remove_tags_should_return_same_string(self):
        # arrange
        self.pipeline = DataProcessingPipeline("hello")
        self.pipeline.add(remove_tags)
        # act

        result = self.pipeline.target_string

        # assert
        self.assertEqual(result,"hello")


    def test_remove_br_should_return_same_string(self):
        # arrange
        self.pipeline = DataProcessingPipeline("hello")
        self.pipeline.add(remove_br)
        # act

        result = self.pipeline.target_string

        # assert
        self.assertEqual(result,"hello")

    def test_remove_br_should_return_2_white_spaces(self):
        # arrange
        self.pipeline = DataProcessingPipeline("<br/><br/>")
        self.pipeline.add(remove_br)
        # act

        result = self.pipeline.target_string

        # assert
        self.assertEqual(result,"  ")

    def test_remove_br_should_return_string_without_br(self):
        # arrange
        self.pipeline = DataProcessingPipeline("<br/>hello<br/>")
        self.pipeline.add(remove_br)
        # act

        result = self.pipeline.target_string

        # assert
        self.assertEqual(result," hello ")

    def test_remove_dash_and_space_should_return_string_without_dash_and_space(self):
        # arrange
        self.pipeline = DataProcessingPipeline("- hello!- ")
        self.pipeline.add(remove_dash_and_space)
        # act

        result = self.pipeline.target_string

        # assert
        self.assertEqual("hello!",result)

    def test_remove_dash_and_space_should_return_empty_string(self):
        # arrange
        self.pipeline = DataProcessingPipeline("- - ")
        self.pipeline.add(remove_dash_and_space)
        # act

        result = self.pipeline.target_string

        # assert
        self.assertEqual("", result)

    def test_remove_dash_and_space_should_return_same_string(self):
        # arrange
        self.pipeline = DataProcessingPipeline("hello world")
        self.pipeline.add(remove_dash_and_space)
        # act

        result = self.pipeline.target_string

        # assert
        self.assertEqual("hello world", result)

    def test_remove_dash_should_return_same_string(self):
        # arrange
        self.pipeline = DataProcessingPipeline("hello world")
        self.pipeline.add(remove_dash)
        # act

        result = self.pipeline.target_string

        # assert
        self.assertEqual("hello world", result)

    def test_remove_dash_should_return_white_space(self):
        # arrange
        self.pipeline = DataProcessingPipeline("-")
        self.pipeline.add(remove_dash)
        # act

        result = self.pipeline.target_string

        # assert
        self.assertEqual(" ", result)

    def test_remove_dash_should_return_string_witout_dashes(self):
        # arrange
        self.pipeline = DataProcessingPipeline("-hello world---")
        self.pipeline.add(remove_dash)
        # act

        result = self.pipeline.target_string

        # assert
        self.assertEqual(" hello world   ", result)

if __name__ == '__main__':
    unittest.main()
