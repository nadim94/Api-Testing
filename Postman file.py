
pm.test("Body Peremiter First Value match", function () {
    pm.expect(pm.response.text()).to.include("userId");
});
pm.test("Body Peremiter Second Value match", function () {
    pm.expect(pm.response.text()).to.include("title");
});

pm.test("Body Peremiter Third Value match", function () {
    pm.expect(pm.response.text()).to.include("body");
});


pm.test("First User Id Check", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData[0].userId).to.eql(1);
});

pm.test("First Id Check", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData[0].id).to.eql(1);
});

pm.test("First Title Check", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData[0].title).to.eql("sunt aut facere repellat provident occaecati excepturi optio reprehenderit");
});

pm.test("First Body check", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData[0].body).to.eql("quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto");
});

pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response time is less than 200ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(150);
});

pm.test("First Id Check for Second Array of Json Value", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData[1].id).to.eql(2);
});

var schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "userId": 1,
            "id": 1,
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
        }
    ],
    "required": [
        "userId",
        "id",
        "title",
        "body"
    ],
    "properties": {
        "userId": {
            "$id": "#/properties/userId",
            "type": "integer",
            "title": "The userId schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1
            ]
        },
        "id": {
            "$id": "#/properties/id",
            "type": "integer",
            "title": "The id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1
            ]
        },
        "title": {
            "$id": "#/properties/title",
            "type": "string",
            "title": "The title schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
            ]
        },
        "body": {
            "$id": "#/properties/body",
            "type": "string",
            "title": "The body schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
            ]
        }
    },
    "additionalProperties": true
};
var jsonData_schema_check = pm.response.json();
pm.test('Schema is valid', function () {
    pm.expect(tv4.validate(jsonData_schema_check, schema));
});
