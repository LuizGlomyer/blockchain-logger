// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

contract UserInteractions {
    address owner;
    mapping(string => string[]) public interactions;

    constructor() {
        owner = msg.sender;
    }

    event SaveSender(address sender);

    function logMessage(string memory user_id, string memory action) public {
        interactions[user_id].push(action);
    }

    /*
    function logMessage(string memory user_id, string memory action) public {
        require(msg.sender == owner);
        interactions[user_id].push(action);
    }
    */

    function retrieveInteractions(string memory user_id)
        public
        view
        returns (string[] memory)
    {
        require(msg.sender == owner);
        return interactions[user_id];
    }
}
