var add = function (a) {
    return function (b) {
        return a + b;
    };
};

var hello = add('Hello ');

console.log(hello('World'));