import pytest

from models.card import Card


@pytest.mark.parametrize(
    "rank, suit",
    [
        (rank, suit)
        for rank in Card.RANKS
        + [rank.lower() for rank in Card.RANKS]
        + [rank.upper() for rank in Card.RANKS]
        for suit in Card.SUITS
    ],
)
def test_card_valid(rank, suit):
    card = Card(rank, suit)
    assert card.rank == rank.capitalize()
    assert card.suit == suit.capitalize()
    assert card.value == Card.VALUES[rank.capitalize()]


@pytest.mark.parametrize("rank", ["1", "11", "", 1, "karalius", None])
def test_card_invalid_rank(rank):
    with pytest.raises(ValueError) as e:
        Card(rank, "Hearts")
    assert "Invalid rank" in str(e.value)


@pytest.mark.parametrize("suit", [1, "", "bugnai", None])
def test_card_invalid_suit(suit):
    with pytest.raises(ValueError) as e:
        Card("2", suit)
    assert "Invalid suit" in str(e.value)


@pytest.mark.parametrize(
    "rank, suit, value",
    [
        ("2", "Hearts", 2),
        ("6", "Diamonds", 6),
        ("10", "Clubs", 10),
        ("Jack", "Spades", 11),
        ("Queen", "Hearts", 12),
        ("King", "Diamonds", 13),
        ("Ace", "Clubs", 14),
    ],
)
def test_card_valid_value(rank, suit, value):
    card = Card(rank, suit)
    assert card.value == value