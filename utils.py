from template_lib.utils import logging_utils


def redirect_stdout_to_logger(logfile):
  logger = logging_utils.get_logger(logfile)
  logging_utils.redirect_print_to_logger(logger)