import altair as alt
import numpy as np


# def damage_mean(damage, samples):
#     parts = damage.split('d')
#     rolls = int(parts[0])
#
#     if '+' in parts[1]:
#         die, modifier = int(parts[1].split('+')[0]), int(parts[1].split('+')[1])
#     else:
#         die, modifier = int(parts[1]), 0
#
#     attacks = np.random.randint(1, die + 1, (samples, rolls)).sum(axis=1) + modifier
#     mean = np.mean(attacks)
#
#     return mean


def Chart(df, x, y, target):
    chart = alt.Chart(df, title=f"{x} by {y} and {target}").mark_point().encode(
        y=y,
        x=x,
        color=alt.Color(target, scale=alt.Scale(scheme='lightgreyred'))
    )
    chart = chart.configure_view(fill='#252525')
    return chart.to_json()
