from eth2.beacon.fork_choice import (
    ForkChoiceScoring,
    higher_slot_scoring,
)
from eth2.beacon.state_machines.base import (
    BeaconStateMachine,
)
from eth2.beacon.state_machines.forks.serenity.blocks import (
    SerenityBeaconBlock,
    create_serenity_block_from_parent,
)
from eth2.beacon.state_machines.forks.serenity.state_transitions import (
    SerenityStateTransition,
)
from eth2.beacon.state_machines.forks.serenity.states import (
    SerenityBeaconState,
)
from eth2.beacon.types.blocks import (
    BaseBeaconBlock,
)
from eth2.beacon.typing import (
    FromBlockParams,
)

from .configs import (
    XIAO_LONG_BAO_CONFIG,
)


class XiaoLongBaoStateMachine(BeaconStateMachine):
    # fork name
    fork = 'xiao_long_bao'
    config = XIAO_LONG_BAO_CONFIG

    # classes
    block_class = SerenityBeaconBlock
    state_class = SerenityBeaconState
    state_transition_class = SerenityStateTransition

    # methods
    @staticmethod
    def create_block_from_parent(parent_block: BaseBeaconBlock,
                                 block_params: FromBlockParams) -> BaseBeaconBlock:
        return create_serenity_block_from_parent(parent_block, block_params)

    def get_fork_choice_scoring(self) -> ForkChoiceScoring:
        return higher_slot_scoring
