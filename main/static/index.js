const createBtn = document.querySelector('.create')
const tareas = document.querySelectorAll('.tarea')
const editBtn = document.querySelectorAll('.fa-pencil')
const deleteBtn = document.querySelectorAll('.fa-trash-can')
const idTask = document.querySelectorAll('#id-tarea')
const actualTitle = document.querySelectorAll('.tituloTarea')
const actualDesc = document.querySelectorAll('.desc')

tareas.forEach((tarea,index) =>{
    //console.log(tarea)
    //console.log('index ---')
    //console.log(index)
    //console.log(idTask)
    //console.log(editBtn[index])    
    //console.log(deleteBtn[index])
    //console.log(idTask[index])    
    //console.log(actualTitle[index].textContent)
    //console.log(actualDesc[index].textContent)

    editBtn[index].addEventListener('click',()=>{
        createLabel('editar',idTask[index].value,index)
    })
    deleteBtn[index].addEventListener('click',()=>{
        deleteLabel(idTask[index].value,index)
    })
})

createBtn.addEventListener('click',()=>{
    //console.log('recon')
    createLabel('crear')
})

const createLabel = (method,id,index) =>{

    let difuminador = document.createElement('div')
    let labelCont = document.createElement('div')
    let titleEditing = document.createElement('div')
    let inputsCont = document.createElement('div')
    let newTitle = document.createElement('div')
    let inputNewText = document.createElement('input')
    let newDescription = document.createElement('div')
    let inputNewDescription = document.createElement('textarea')
    let btnConts = document.createElement('div')
    let saveBtn = document.createElement('input')
    let cancelBtn = document.createElement('input')

    document.body.appendChild(difuminador)
    difuminador.appendChild(labelCont)
    labelCont.appendChild(titleEditing)
    labelCont.appendChild(inputsCont)
    inputsCont.appendChild(newTitle)
    inputsCont.appendChild(inputNewText)
    inputsCont.appendChild(newDescription)
    inputsCont.appendChild(inputNewDescription)
    labelCont.appendChild(btnConts)
    btnConts.appendChild(cancelBtn)
    btnConts.appendChild(saveBtn)

    difuminador.classList.add('difuminador')
    labelCont.classList.add('labelCont')
    titleEditing.classList.add('titleEditing')
    inputsCont.classList.add('inputsCont')
    newTitle.classList.add('newTitle')
    inputNewText.classList.add('inputNewTitle')
    newDescription.classList.add('newDescription')
    inputNewDescription.classList.add('inputnewDescription')
    btnConts.classList.add('btnCont')
    cancelBtn.classList.add('btn')
    cancelBtn.classList.add('cancelBtn')
    saveBtn.classList.add('btn')
    saveBtn.classList.add('saveBtn')

    if (method == 'crear'){
        //crear
        titleEditing.textContent = 'Creando Nueva Tarea'
        newTitle.textContent = 'Ingresa un titulo: '
        inputNewText.type = 'text'
        inputNewText.placeholder = 'Nuevo Titulo'
        inputNewText.required = 'true'
        inputNewDescription.cols = '22'
        inputNewDescription.rows = '5'
        newDescription.textContent = 'Ingresa una Descripcion:'
        inputNewDescription.placeholder = 'Nueva descripcion'
        saveBtn.type = 'button'
        saveBtn.value = 'Save'
        cancelBtn.type = 'button'
        cancelBtn.value = 'Cancel'
        let cancel = document.querySelector('.cancelBtn')
        let save = document.querySelector('.saveBtn')

        save.addEventListener('click',()=>{
            let newTitle = document.querySelector('.inputNewTitle').value
            let newDescription = document.querySelector('.inputnewDescription').value
            console.log('save recon')
            if(inputNewText.value.length > 1){
                fetch('http://localhost:3001/create/',{
                    method:'GET',
                    headers: {"Content-Type": "application/json"}
                })
                .then(data => data.json())
                .then(res => {
                    console.log(res)
                    let token = res.token
                    fetch('http://localhost:3001/create/', {
                        method: 'POST',
                        headers: {
                            "Content-Type": "application/json",
                            'X-CSRFToken': token
                        },
                        body: JSON.stringify({'title': newTitle, 'description': newDescription})
                    })
                
                })
                difuminador.remove()
                //window.location.href = "/view_tasks/"
                //history.go()
            }
            else{
                console.log('imposible guardar')
            }
        })
        cancel.addEventListener('click',()=>{
            console.log('recon')
            difuminador.remove()
        })
    }
    else if(method == 'editar'){
        titleEditing.textContent = `Editando: ${actualTitle[index].textContent}`
        newTitle.textContent = 'Ingresa un nuevo titulo: '
        inputNewText.type = 'text'
        inputNewText.value = actualTitle[index].textContent
        inputNewText.placeholder = 'Nuevo Titulo'
        inputNewText.required = 'true'
        inputNewDescription.cols = '22'
        inputNewDescription.rows = '5'
        inputNewDescription.value = actualDesc[index].textContent
        newDescription.textContent = 'Ingresa una nueva Descripcion:'
        inputNewDescription.placeholder = 'Nueva descripcion'
        saveBtn.type = 'button'
        saveBtn.value = 'Save'
        cancelBtn.type = 'button'
        cancelBtn.value = 'Cancel'
        let cancel = document.querySelector('.cancelBtn')
        let save = document.querySelector('.saveBtn')
    
        save.addEventListener('click',()=>{
            let newTitle = document.querySelector('.inputNewTitle').value
            let newDescription = document.querySelector('.inputnewDescription').value
            //console.log('save recon')
            if(inputNewText.value.length > 1){
                fetch('http://localhost:3001/create/',{
                    method:'GET',
                    headers: {"Content-Type": "application/json"}
                })
                .then(data => data.json())
                .then(res => {
                    console.log(res)
                    let token = res.token
                    fetch('http://localhost:3001/edit/', {
                        method: 'POST',
                        headers: {
                            "Content-Type": "application/json",
                            'X-CSRFToken': token
                        },
                        body: JSON.stringify({'id':id,'title': newTitle, 'description': newDescription})
                    })
                    
                })
                difuminador.remove()
                //window.location.href = "/view_tasks/"
                //history.go()
            }
            else{
                console.log('imposible actualizar')
            }
        })
        cancel.addEventListener('click',()=>{
            console.log('cancel recon')
            difuminador.remove()
        })
    }
}

const deleteLabel = (id,index) =>{
    let difuminador = document.createElement('div')
    let labelDeleteCont = document.createElement('div')
    let titleDeleting = document.createElement('div')
    let textDeleting = document.createElement('div')
    let btnDeleteConts = document.createElement('div')
    let acceptBtn = document.createElement('input')
    let cancelDelBtn = document.createElement('input')

    document.body.appendChild(difuminador)
    difuminador.appendChild(labelDeleteCont)
    labelDeleteCont.appendChild(titleDeleting)
    labelDeleteCont.appendChild(textDeleting)
    labelDeleteCont.appendChild(btnDeleteConts)
    btnDeleteConts.appendChild(cancelDelBtn)
    btnDeleteConts.appendChild(acceptBtn)

    difuminador.classList.add('difuminador')
    labelDeleteCont.classList.add('labelDeleteCont')
    titleDeleting.classList.add('titleDeleting')
    textDeleting.classList.add('textDeleting')
    btnDeleteConts.classList.add('btnDeleteConts')
    acceptBtn.classList.add('acceptBtn')
    acceptBtn.classList.add('btn')
    cancelDelBtn.classList.add('cancelDelBtn')
    cancelDelBtn.classList.add('btn')

    titleDeleting.textContent = `Estas por eliminar la tarea con id: ${id}, ${actualTitle[index].textContent}`
    textDeleting.textContent = '¿Estas seguro que quieres continuar?'
    acceptBtn.type = 'button'
    acceptBtn.value = 'Aceptar'
    cancelDelBtn.type = 'button'
    cancelDelBtn.value = 'Cancelar'
    let cancel = document.querySelector('.cancelDelBtn')
    let accept = document.querySelector('.acceptBtn')
    accept.addEventListener('click',()=>{
        fetch('http://localhost:3001/delete/',{
            method:'GET',
            headers: {"Content-Type": "application/json"}
        })
        .then(data => data.json())
        .then(res => {
            //console.log('post enviado')
            let token = res.token
            fetch('http://localhost:3001/delete/', {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                    'X-CSRFToken': token
                },
                body: JSON.stringify({'id':id})
            })    
        })
        difuminador.remove()
        window.location.href = "/view_tasks/"
        history.go()
    })
    cancel.addEventListener('click',()=>{
        difuminador.remove()
    })
}