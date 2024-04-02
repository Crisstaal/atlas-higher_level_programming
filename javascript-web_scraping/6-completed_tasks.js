#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
    if (!error && response.statusCode === 200) {
        try {
            const todos = JSON.parse(body);
            const completed = {};
            todos.forEach((todo) => {
                if (todo.completed) {
                    if (completed[todo.userId] === undefined) {
                        completed[todo.userId] = 1;
                    } else {
                        completed[todo.userId]++;
                    }
                }
            });

            const completedTasks = Object.keys(completed).length;
            if (completedTasks > 0) {
                for (const userId in completed) {
                    console.log(`'${userId}': ${completed[userId]},`);
                }
            } else {
                console.log("{ }");
            }

        } catch (parseError) {
            console.error('Error parsing JSON:', parseError);
        }
    } else {
        console.error('Error:', error);
    }
});
