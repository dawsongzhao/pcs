from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from pcs.cli.constraint import command
from pcs.cli.constraint_ticket import parse_args, console_report

def create_with_set(lib, argv, modificators):
    command.create_with_set(
        lib.constraint_ticket.set,
        argv,
        modificators,
    )

def add(lib, argv, modificators):
    ticket, resource_id, resource_role, options = parse_args.parse_add(argv)
    lib.constraint_ticket.add(
        ticket,
        resource_id,
        resource_role,
        options,
        autocorrection_allowed=modificators["autocorrect"],
        resource_in_clone_alowed=modificators["force"],
        duplication_alowed=modificators["force"],
    )

def show(lib, argv, modificators):
    print("\n".join(command.show(
        "Ticket Constraints:",
        lib.constraint_ticket.show,
        console_report.constraint_plain,
        modificators,
    )))