import re, os

from template_lib.utils.plot_utils import MatPlot


def parse_logfile(args, myargs):
  config = getattr(myargs.config, args.command)
  matplot = MatPlot()
  fig, ax = matplot.get_fig_and_ax()
  if len(config.logfiles) == 1:
    logfiles = config.logfiles * len(config.re_strs)
  for logfile, re_str in zip(logfiles, config.re_strs):
    RE_STR = re.compile(re_str)
    _, step = matplot.parse_logfile_using_re(
      logfile=logfile, re_str=re.compile('Step (\d*)'))
    (idx, val) = matplot.parse_logfile_using_re(logfile=logfile, re_str=RE_STR)
    ax.plot(step, val, label=re_str)
  ax.legend()
  matplot.save_to_png(
    fig, filepath=os.path.join(args.outdir, config.title + '.png'))
  pass