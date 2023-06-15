const notice_btn = document.getElementById("notices")
const create_btn = document.getElementById("create")
const api_btn = document.getElementById("api")
const submit = document.getElementById('submit')
const user_id = document.getElementById('user_id')
const notice_list = document.querySelector('.notice_list')

//handle focusing content on aside button click
function handleFocus(e, focusClass) {
    if (e != null)
        e.preventDefault();
    const current_focus = document.querySelector('.focus');
    current_focus.classList.remove('focus');
    const new_focus = document.querySelector(focusClass);
    new_focus.classList.add('focus');
}

//updates the list of Notices on the frontend
function updateNotice(Notices) {
     Notices.map(notice => {
        const notice_item = document.createElement('li');
        notice_item.className = "notice_item";
        const btn = document.createElement('button');
        btn.className = "btn";
        btn.dataset.id = notice.id;
        btn.textContent = notice.title;
        const date = document.createElement('span');
        date.className = "date"
        const today = new Date(notice.created_at);
        date.textContent = today.toDateString();
        btn.append(date);
        notice_item.append(btn);

        const contain = document.createElement('div');
        contain.className = "contain";
        const p = document.createElement('p');
        p.textContent = notice.text;
        contain.append(p);
        notice_item.append(contain);
        notice_list.append(notice_item);

        btn.addEventListener('click', (e) => {
            const target = e.target.nextElementSibling;
            target.classList.toggle('show');
        });
    });
}


let Notices = []
const url = `http://localhost:5001/api/v1/user/${user_id.dataset.id}/notices`;
fetch(url)
.then(response => response.json())
.then(data => {
    Notices = data;
    updateNotice(Notices);
})


submit.addEventListener('click', (e) => {
    e.preventDefault();
    let data = {}
    const title = document.getElementById('title');
    const text = document.getElementById('text');

    if (text.value == "" || title.value == "") return;

    data["title"] = title.value;
    data["text"] = text.value
    
    let url = `http://localhost:5001/api/v1/user/${user_id.dataset.id}/notice`
    data = JSON.stringify(data)
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: data
    })
    .then(response => response.json())
    .then(data => {
        Notices.push(data)
        notice_list.innerHTML = "";
        Notices.reverse();
        updateNotice(Notices);
    })
    handleFocus(null, '.notices');
    text.value = ""
    title.value = ""
})


api_btn.addEventListener('click', (e) => {
    handleFocus(e, '.api');
})

notice_btn.addEventListener('click', (e) => {
    handleFocus(e, '.notices');
})

create_btn.addEventListener('click', (e) => {
    handleFocus(e, '.create');
})
