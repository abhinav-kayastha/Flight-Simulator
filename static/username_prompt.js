'use strict';

const username = prompt('Enter your username.')

const p = document.getElementById('username')

p.insertAdjacentText('afterend', `${username}`)