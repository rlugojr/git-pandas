from gitpandas.utilities.plotting import plot_cumulative_blame
from gitpandas import ProjectDirectory

g = ProjectDirectory(working_dir=['git://github.com/rhiever/tpot.git'])
blame = g.cumulative_blame(branch='master', extensions=['py', 'html', 'sql', 'md'], by='committer', limit=None, skip=None)
plot_cumulative_blame(blame)