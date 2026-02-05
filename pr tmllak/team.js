function showPage(pageName) {
    // 1. إخفاء جميع الصفحات
    const allPages = document.querySelectorAll('.page');
    allPages.forEach(p => p.classList.remove('active'));

    // 2. إزالة حالة "النشط" من روابط القائمة
    const allLinks = document.querySelectorAll('.sidebar li');
    allLinks.forEach(l => l.classList.remove('active'));

    // 3. إظهار الصفحة المختارة وتفعيل الرابط الخاص بها
    if (pageName === 'home') {
        document.getElementById('home-page').classList.add('active');
        document.getElementById('link-home').classList.add('active');
    } else if (pageName === 'team') {
        document.getElementById('team-page').classList.add('active');
        document.getElementById('link-team').classList.add('active');
    }
}