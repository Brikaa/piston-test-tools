const fs = require('fs');

(async () => {
    const file_name = process.argv[2];
    const [_, language] = file_name.split('.');
    const URL = 'http://127.0.0.1:2000/api/v2/execute';
    const file = fs.readFileSync(file_name);
    const requests = [];
    const no_requests = parseInt(process.argv[3]);

    for (let i = 0; i < no_requests; ++i) {
        requests.push(
            fetch(URL, {
                headers: {
                    'CONTENT-TYPE': 'application/json'
                },
                method: 'POST',
                body: JSON.stringify({
                    language,
                    version: '*',
                    files: [{ content: file.toString() }]
                })
            }).then((res) => res.json())
        );
    }

    const responses = await Promise.all(requests);
    console.log(responses);
})();
