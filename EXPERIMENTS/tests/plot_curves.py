import unittest, os, sys
import argparse

os.chdir('..')
from template_lib import utils


class TestPlot(unittest.TestCase):
  def test_plot_pgd_adv_acc(self):
    """
    Usage:
        source activate tf_1_12
        export CUDA_VISIBLE_DEVICES=0
        export PORT=6006
        export TIME_STR=1
        export PYTHONPATH=../submodule:../cnn:..
        python -c "import plot_curves; \
        plot_curves.TestPlot().test_plot_pgd_adv_acc()"

    :return:
    """
    if 'CUDA_VISIBLE_DEVICES' not in os.environ:
      os.environ['CUDA_VISIBLE_DEVICES'] = '5'
    if 'PORT' not in os.environ:
      os.environ['PORT'] = '6011'
    if 'TIME_STR' not in os.environ:
      os.environ['TIME_STR'] = '0'

    # func name
    outdir = os.path.join('results/plot', sys._getframe().f_code.co_name)
    myargs = argparse.Namespace()

    def build_args():
      argv_str = f"""
            --config configs/config.yaml
            --command plot_pgd_adv_acc
            --resume False --resume_path None
            --resume_root None
            """
      parser = utils.args_parser.build_parser()
      if len(sys.argv) == 1:
        args = parser.parse_args(args=argv_str.split())
      else:
        args = parser.parse_args()
      args.CUDA_VISIBLE_DEVICES = os.environ['CUDA_VISIBLE_DEVICES']
      args = utils.config_utils.DotDict(vars(args))
      return args, argv_str
    args, argv_str = build_args()

    args.outdir = outdir
    args, myargs = utils.config.setup_args_and_myargs(args=args, myargs=myargs)
    from TOOLS import parse_logfile
    parse_logfile.parse_logfile(args, myargs)
    input('End %s' % outdir)
    return
