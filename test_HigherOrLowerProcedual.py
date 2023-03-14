# tests for HigherOrLowerProcedual

from unittest import TestCase, mock, main

from HigherOrLowerProcedural import (
    get_card, prediction,
    calculate_card_value,
    create_deck
)


class TestMyHigherOrLower(TestCase):
    """
    Ideas:
    1. Проверить количесво кард в колоде(листе) == 52 +
    2. Проверить на повторения+
    3. Check same value different suits.+
    3 сценария возвращают 20/ 10 False 9 & 1 True 2 & 9 True 9
    3 сценария возващают -15/ 10 True > 9 & 1 False > 1 & 9 False 9
    """

    @mock.patch('HigherOrLowerProcedural.create_deck')
    def test_prediction_10_and_False__success(self, my_mock):
        mocked_deck = my_mock.return_value = [
            ('10', 'Spades'), ('Ace', 'Hearts')
        ]
        my_mocked_card = get_card(my_mock.return_value)
        test_prediction = prediction(10, False, mocked_deck)
        self.assertEqual(1, calculate_card_value(my_mocked_card))
        self.assertEqual(test_prediction, 20)

    @mock.patch('HigherOrLowerProcedural.create_deck')
    def test_prediction_9_and_False_same_values__success(self, my_mock):
        mocked_deck = my_mock.return_value = [
            ('9', 'Spades'), ('9', 'Hearts')
        ]
        my_mocked_card = get_card(my_mock.return_value)
        test_prediction = prediction(9, False, mocked_deck)
        self.assertEqual(9, calculate_card_value(my_mocked_card))
        self.assertEqual(test_prediction, 20)

    @mock.patch('HigherOrLowerProcedural.create_deck')
    def test_prediction_9_and_True_same_values__failed(self, my_mock):
        mocked_deck = my_mock.return_value = [('9', 'Spades'), ('9', 'Hearts')]
        my_mocked_card = get_card(my_mock.return_value)
        test_prediction = prediction(9, True, mocked_deck)
        self.assertEqual(9, calculate_card_value(my_mocked_card))
        self.assertEqual(test_prediction, -15)

    @mock.patch('HigherOrLowerProcedural.create_deck')
    def test_prediction_10_and_True__failed(self, my_mock):
        mocked_deck = my_mock.return_value = [
            ('10', 'Spades'), ('10', 'Hearts')
        ]
        my_mocked_card = get_card(my_mock.return_value)
        test_prediction = prediction(10, True, mocked_deck)
        self.assertEqual(10, calculate_card_value(my_mocked_card))
        self.assertEqual(test_prediction, -15)

    @mock.patch('HigherOrLowerProcedural.create_deck')
    def test_prediction_4_and_False__failed(self, my_mock):
        mocked_deck = my_mock.return_value = [('4', 'Spades'), ('3', 'Hearts')]
        my_mocked_card = get_card(my_mock.return_value)
        test_prediction = prediction(3, False, mocked_deck)
        self.assertEqual(3, calculate_card_value(my_mocked_card))
        self.assertEqual(test_prediction, -15)

    def test_number_of_in_deck__success(self):
        test_deck = create_deck(2)
        self.assertEqual(2, len(test_deck))

    @mock.patch('HigherOrLowerProcedural.SUIT_TUPLE')
    @mock.patch('HigherOrLowerProcedural.RANK_TUPLE')
    def test_own_deck__success(self, mock_rank, mock_suit):
        mock_rank.return_value = ('4', '3')
        mock_suit.return_value = ('Hearts',)
        test_deck = create_deck(
            suits=mock_suit.return_value, ranks=mock_rank.return_value
        )
        self.assertEqual(2, len(test_deck))

    @mock.patch('HigherOrLowerProcedural.SUIT_TUPLE')
    @mock.patch('HigherOrLowerProcedural.RANK_TUPLE')
    def test_own_deck_same_ranks__failed(self, mock_rank, mock_suit):
        mock_rank.return_value = ('4', '4')
        mock_suit.return_value = ('Hearts',)
        test_deck = create_deck(
            suits=mock_suit.return_value, ranks=mock_rank.return_value
        )
        self.assertNotEqual(2, len(test_deck))


if __name__ == "__main__":
    main()
