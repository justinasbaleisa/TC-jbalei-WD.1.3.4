import pytest

from models.card import Card
from models.hand import Hand
from models.deck import Deck


@pytest.mark.parametrize(
    "cards",
    [
        *[Card(rank, suit) for rank in Card.RANKS for suit in Card.SUITS],
        [],
        Deck().cards,
    ],
)
def test_hand_valid(cards):
    hand = Hand(cards)

    if isinstance(cards, Card):
        assert hand.cards == [cards]
    elif isinstance(cards, list):
        assert hand.cards == cards


@pytest.mark.parametrize(
    "cards",
    [
        "Invalid type",
        1,
        None,
        [
            *[Card(rank, suit) for rank in Card.RANKS for suit in Card.SUITS][:-1],
            "Invalid type",
        ],
    ],
)
def test_hand_invalid(cards):
    with pytest.raises(ValueError) as e:
        Hand(cards)
    assert "Invalid card" in str(e.value)


@pytest.mark.parametrize(
    "cards",
    [*[Card(rank, suit) for rank in Card.RANKS for suit in Card.SUITS], Deck().cards],
)
def test_add_cards_valid(cards):
    hand = Hand([])
    hand.add_cards(cards)
    if isinstance(cards, Card):
        assert hand.cards == [cards]
    elif isinstance(cards, list):
        assert hand.cards == cards


@pytest.mark.parametrize(
    "cards",
    [
        "Invalid type",
        1,
        None,
        [
            *[Card(rank, suit) for rank in Card.RANKS for suit in Card.SUITS][:-1],
            "Invalid type",
        ],
    ],
)
def test_add_cards_invalid(cards):
    hand = Hand([])
    with pytest.raises(ValueError) as e:
        hand.add_cards(cards)
    assert "Invalid card" in str(e.value)


def test_add_cards_invalid_duplicate_cards():
    hand = Hand([Card("Ace", "Hearts")])
    with pytest.raises(ValueError) as e:
        hand.add_cards(Card("Ace", "Hearts"))
    assert "Duplicate card" in str(e.value)
    assert len(hand.cards) == 1
    assert hand.cards.count(Card("Ace", "Hearts")) == 1


def test_play_card_valid():
    deck = Deck()
    hand = Hand(deck.cards)
    hand_size = len(hand.cards)
    for index in range(hand_size):
        hand.play_card()
        assert len(hand.cards) == hand_size - (index + 1)


def test_play_card_invalid():
    hand = Hand([])
    assert len(hand.cards) == 0
    with pytest.raises(ValueError) as e:
        hand.play_card()
    assert "Cannot play a card from an empty hand" in str(e.value)
