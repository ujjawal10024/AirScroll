def is_thumbs_up(hand):
    thumb_up = hand.landmark[4].y < hand.landmark[3].y

    fingers_folded = (
        hand.landmark[8].y > hand.landmark[6].y and
        hand.landmark[12].y > hand.landmark[10].y and
        hand.landmark[16].y > hand.landmark[14].y and
        hand.landmark[20].y > hand.landmark[18].y
    )

    return thumb_up and fingers_folded


def is_open_palm(hand):
    return (
        hand.landmark[8].y < hand.landmark[6].y and
        hand.landmark[12].y < hand.landmark[10].y and
        hand.landmark[16].y < hand.landmark[14].y and
        hand.landmark[20].y < hand.landmark[18].y
    )
