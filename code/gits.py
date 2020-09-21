
import os
import sys
import argparse
from gits_profile import gits_set_profile
from gits_pr_update import gits_pr_update
from gits_rebase import gits_rebase
from gits_reset import gits_reset

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

gits_profile_subparser = subparsers.add_parser('profile', help='profie help')
gits_profile_subparser.set_defaults(func=gits_set_profile)
gits_profile_subparser.add_argument('--email', required=True, help='email to be used')
gits_profile_subparser.add_argument('--name', required=True, help='name to be used')
print(gits_profile_subparser.parse_args(['--email']))

gits_pr_subparser= subparsers.add_parser('sync', help='sync help')
print("test")
gits_pr_subparser.set_defaults(func=gits_pr_update)
gits_pr_subparser.add_argument('--upstream', nargs='?')


gits_pr_subparser= subparsers.add_parser('rebase', help='sync help')
gits_pr_subparser.set_defaults(func=gits_rebase)


gits_reset_subparser= subparsers.add_parser('reset', help='sync help')
gits_reset_subparser.set_defaults(func=gits_reset)
gits_reset_subparser.add_argument('--branch', required=True, help='branch to be used')


args = parser.parse_args()
args.func(args)

