import os
import sys
import unittest
import argparse

os.chdir('..')
from template_lib import utils


def _parse_args(argv_str):
  parser = utils.args_parser.build_parser()
  if len(sys.argv) == 1:
    args = parser.parse_args(args=argv_str.split())
  else:
    args = parser.parse_args()
  args.CUDA_VISIBLE_DEVICES = os.environ['CUDA_VISIBLE_DEVICES']
  args = utils.config_utils.DotDict(vars(args))
  return args


class Testing_mnist_challenge(unittest.TestCase):

  def test_pgd_attack_natural(self):
    """
    Usage:
        export CUDA_VISIBLE_DEVICES=2,3,4,5
        export PORT=6006
        export TIME_STR=1
        export PYTHONPATH=../../submodule:..
        python -c "import test_mnist_challenge; \
        test_mnist_challenge.Testing_mnist_challenge().test_pgd_attack_natural()"

    :return:
    """
    if 'CUDA_VISIBLE_DEVICES' not in os.environ:
      os.environ['CUDA_VISIBLE_DEVICES'] = '5'
    if 'PORT' not in os.environ:
      os.environ['PORT'] = '6011'
    if 'TIME_STR' not in os.environ:
      os.environ['TIME_STR'] = '0'
    # func name
    outdir = os.path.join('results/', sys._getframe().f_code.co_name)
    myargs = argparse.Namespace()
    argv_str = f"""
          --config ./configs/config.yaml 
          --command pgd_attack_natural
          --resume False --resume_path None
          --resume_root None
          """
    args = _parse_args(argv_str)

    args.outdir = outdir
    args, myargs = utils.config.setup_args_and_myargs(args=args, myargs=myargs)
    import pgd_attack
    pgd_attack.run(args, myargs)
    input('End %s' % outdir)
    return

  def test_run_attack_natural(self):
    """
    Usage:
        export CUDA_VISIBLE_DEVICES=2,3,4,5
        export PORT=6006
        export TIME_STR=1
        export PYTHONPATH=../../submodule:..
        python -c "import test_mnist_challenge; \
        test_mnist_challenge.Testing_mnist_challenge().test_run_attack_natural()"

    :return:
    """
    if 'CUDA_VISIBLE_DEVICES' not in os.environ:
      os.environ['CUDA_VISIBLE_DEVICES'] = '5'
    if 'PORT' not in os.environ:
      os.environ['PORT'] = '6011'
    if 'TIME_STR' not in os.environ:
      os.environ['TIME_STR'] = '0'
    outdir = os.path.join('results/', sys._getframe().f_code.co_name)
    myargs = argparse.Namespace()
    argv_str = f"""
          --config ./configs/config.yaml 
          --command run_attack_natural
          --resume False --resume_path None
          --resume_root None
          """
    args = _parse_args(argv_str)

    args.outdir = outdir
    args, myargs = utils.config.setup_args_and_myargs(args=args, myargs=myargs)
    import run_attack
    run_attack.run(args, myargs)
    input('End %s' % outdir)
    return

  def test_pgd_attack_adv_trained(self):
    """
    Usage:
        export CUDA_VISIBLE_DEVICES=2,3,4,5
        export PORT=6006
        export TIME_STR=1
        export PYTHONPATH=../../submodule:..
        python -c "import test_mnist_challenge; \
        test_mnist_challenge.Testing_mnist_challenge().test_pgd_attack_adv_trained()"

    :return:
    """
    if 'CUDA_VISIBLE_DEVICES' not in os.environ:
      os.environ['CUDA_VISIBLE_DEVICES'] = '5'
    if 'PORT' not in os.environ:
      os.environ['PORT'] = '6011'
    if 'TIME_STR' not in os.environ:
      os.environ['TIME_STR'] = '0'
    # func name
    outdir = os.path.join('results/', sys._getframe().f_code.co_name)
    myargs = argparse.Namespace()
    argv_str = f"""
          --config ./configs/config.yaml 
          --command pgd_attack_adv_trained
          --resume False --resume_path None
          --resume_root None
          """
    args = _parse_args(argv_str)

    args.outdir = outdir
    args, myargs = utils.config.setup_args_and_myargs(args=args, myargs=myargs)
    import pgd_attack
    pgd_attack.run(args, myargs)
    input('End %s' % outdir)
    return

  def test_run_attack_adv_trained(self):
    """
    Usage:
        export CUDA_VISIBLE_DEVICES=2,3,4,5
        export PORT=6006
        export TIME_STR=1
        export PYTHONPATH=../../submodule:..
        python -c "import test_mnist_challenge; \
        test_mnist_challenge.Testing_mnist_challenge().test_run_attack_adv_trained()"

    :return:
    """
    if 'CUDA_VISIBLE_DEVICES' not in os.environ:
      os.environ['CUDA_VISIBLE_DEVICES'] = '5'
    if 'PORT' not in os.environ:
      os.environ['PORT'] = '6011'
    if 'TIME_STR' not in os.environ:
      os.environ['TIME_STR'] = '0'
    outdir = os.path.join('results/', sys._getframe().f_code.co_name)
    myargs = argparse.Namespace()
    argv_str = f"""
          --config ./configs/config.yaml 
          --command run_attack_adv_trained
          --resume False --resume_path None
          --resume_root None
          """
    args = _parse_args(argv_str)

    args.outdir = outdir
    args, myargs = utils.config.setup_args_and_myargs(args=args, myargs=myargs)
    import run_attack
    run_attack.run(args, myargs)
    input('End %s' % outdir)
    return






