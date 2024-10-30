"""

plot_hypervolume_history
========================

.. autofunction:: optuna.visualization.plot_hypervolume_history

The following code snippet shows how to plot optimization history.

"""

import optuna
from plotly.io import show


def objective(trial):
    x = trial.suggest_float("x", 0, 5)
    y = trial.suggest_float("y", 0, 3)

    v0 = 4 * x**2 + 4 * y**2
    v1 = (x - 5) ** 2 + (y - 5) ** 2
    return v0, v1


study = optuna.create_study(directions=["minimize", "minimize"])
study.optimize(objective, n_trials=50)

reference_point = [100.0, 50.0]
fig = optuna.visualization.plot_hypervolume_history(study, reference_point)
show(fig)