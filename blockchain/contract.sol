// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

contract UserActions {
    mapping(string => string[]) public actions;

    function store(string memory user_id, string memory action) public {
        actions[user_id].push(action);
    }

    function retrieveActions(string memory user_id)
        public
        view
        returns (string[] memory)
    {
        return actions[user_id];
    }
}
