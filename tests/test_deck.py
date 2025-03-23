import pytest

from models.card import Card
from models.deck import Deck


@pytest.mark.parametrize(
    "rank, suit", [(rank, suit) for rank in Card.RANKS for suit in Card.SUITS]
)
def test_deck_valid(rank, suit):
    deck = Deck()
    assert len(deck.cards) == len(Card.RANKS) * len(Card.SUITS)
    assert Card(rank, suit) in deck

    unique_cards = set(str(card) for card in deck.cards)
    assert len(unique_cards) == len(deck.cards)


def test_deck_shuffle():
    deck = Deck()
    original_order = deck.cards[:]
    deck.shuffle()
    assert sorted(deck.cards, key=lambda card: str(card)) == sorted(
        original_order, key=lambda card: str(card)
    )
    assert deck.cards != original_order


def test_deck_deal():
    deck = Deck()
    initial_length = len(deck.cards)
    first_hand, second_hand = deck.deal()
    assert len(first_hand) + len(second_hand) == initial_length
    all_dealt_cards = first_hand + second_hand
    unique_dealt_cards = set(str(card) for card in all_dealt_cards)
    assert len(all_dealt_cards) == len(unique_dealt_cards)


def test_deck_empty_after_deal():
    deck = Deck()
    deck.deal()
    assert len(deck.cards) == 0


def test_repeated_dealing():
    deck = Deck()
    deck.deal()
    with pytest.raises(ValueError) as e:
        deck.deal()
    assert "Not enough" in str(e.value)


def test_shuffle_and_deal():
    deck = Deck()
    deck.shuffle()
    first_hand, second_hand = deck.deal()
    assert len(first_hand) + len(second_hand) == len(Card.RANKS) * len(Card.SUITS)
    unique_cards = set(str(card) for card in first_hand + second_hand)
    assert len(unique_cards) == len(Card.RANKS) * len(Card.SUITS)


def test_partial_deck():
    deck = Deck()
    deck.cards = deck.cards[:10]
    deck.shuffle()
    first_hand, second_hand = deck.deal()
    assert len(first_hand) + len(second_hand) == 10
