#!/usr/bin/env python3

import asyncio
import subprocess

import qubesadmin
import qubesadmin.events

# Intel Ultra 7 155H
P_CORES = '0-7,16-19'
E_CORES = '8-15,20-21'
ALL_CORES = 'all'

tag_perf = 'p-cores'
tag_eff = 'e-cores'
tag_eff_soft = 'e-cores-soft'
tag_perf_soft = 'p-cores-soft'

def _vcpu_pin(name, cores):
    cmd = ['xl', 'vcpu-pin', name, 'all', cores]
    subprocess.run(cmd).check_returncode()

def _vcpu_pin_soft(name, cores):
    cmd = ['xl', 'vcpu-pin', name, 'all', '-', cores]
    subprocess.run(cmd).check_returncode()

def pin_by_tag(vm, event, **kwargs):
    vm = app.domains[str(vm)]
    if tag_perf in list(vm.tags):
        _vcpu_pin(vm.name, P_CORES)
        print(f'Pinned {vm.name} to P-cores')
    if tag_perf_soft in list(vm.tags):
        _vcpu_pin_soft(vm.name, P_CORES)
        print(f'Pinned {vm.name} to P-cores (soft)')
    if tag_eff in list(vm.tags):
        _vcpu_pin(vm.name, E_CORES)
        print(f'Pinned {vm.name} to E-cores')
    if tag_eff_soft in list(vm.tags):
        _vcpu_pin_soft(vm.name, E_CORES)
        print(f'Pinned {vm.name} to E-cores (soft)')

_vcpu_pin("Domain-0", ALL_CORES)
_vcpu_pin_soft("Domain-0", E_CORES)
app = qubesadmin.Qubes()
dispatcher = qubesadmin.events.EventsDispatcher(app)
dispatcher.add_handler('domain-start', pin_by_tag)
asyncio.run(dispatcher.listen_for_events())
