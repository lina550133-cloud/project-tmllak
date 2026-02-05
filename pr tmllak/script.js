// وظيفة التنقل بين الصفحات
function showPage(pageId) {
    // 1. إخفاء جميع الأقسام
    const pages = document.querySelectorAll('.page');
    pages.forEach(p => p.classList.remove('active'));

    // 2. إزالة التحديد من القائمة الجانبية
    const menuLinks = document.querySelectorAll('.sidebar li');
    menuLinks.forEach(link => link.classList.remove('active'));

    // 3. إظهار القسم المطلوب
    const targetPage = document.getElementById(pageId + '-page');
    if (targetPage) {
        targetPage.classList.add('active');
    }

    // 4. تفعيل العنصر المختار في القائمة
    const activeLink = document.getElementById('link-' + pageId);
    if (activeLink) {
        activeLink.classList.add('active');
    }
}

// وظيفة إضافة عضو جديد في صفحة الفريق
function addNewMember() {
    let name = prompt("أدخل اسم العضو الجديد:");
    let email = prompt("أدخل البريد الإلكتروني:");

    if (name && email) {
        const container = document.getElementById('teamContainer');
        const addBtnCard = document.querySelector('.add-card');

        // إنشاء كرت جديد
        const newCard = document.createElement('div');
        newCard.className = 'member-card';
        newCard.innerHTML = `
            <div class="circle-avatar" style="background:#e0d4c0"></div>
            <h3>${name}</h3>
            <p>${email}</p>
            <button class="member-btn">عرض الحساب</button>
        `;

        // إضافته قبل زر الإضافة
        container.insertBefore(newCard, addBtnCard);
    }
}