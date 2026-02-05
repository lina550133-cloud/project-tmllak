function showPage(pageId) {
    // 1. إخفاء كل الصفحات
    const pages = document.querySelectorAll('.page');
    pages.forEach(page => page.classList.remove('active'));

    // 2. إزالة حالة "active" من جميع أزرار القائمة الجانبية
    const menuItems = document.querySelectorAll('.sidebar li');
    menuItems.forEach(item => item.classList.remove('active'));

    // 3. إظهار الصفحة المطلوبة
    document.getElementById(pageId + '-page').classList.add('active');

    // 4. إضافة حالة "active" للزر الذي تم الضغط عليه
    document.getElementById('link-' + pageId).classList.add('active');
}

// دالة إضافة عضو جديد
function addNewMember() {
    let name = prompt("أدخل اسم عضو الفريق الجديد:");
    if (name) {
        const container = document.getElementById('teamContainer');
        const addCard = document.querySelector('.add-btn-card');
        
        const newMember = document.createElement('div');
        newMember.className = 'member-card';
        newMember.innerHTML = `
            <div class="circle-img" style="background:#e0d4c0"></div>
            <h3>${name}</h3>
            <p>new.member@tmllak.com</p>
            <button class="main-btn">عرض الحساب</button>
        `;
        container.insertBefore(newMember, addCard);
    }
}