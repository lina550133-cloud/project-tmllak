/**
 * تواصل مع الباك اند – /api/v1
 * إذا الفرونت من نفس السيرفر (مثلاً :8000) يستخدم نفس المنشأ؛ وإلا غيّر API_BASE.
 * يخزن: access_token, refresh_token, user في localStorage
 */
const API_BASE = window.location.origin + '/api/v1';

function getToken() {
  return localStorage.getItem('access_token');
}

function getRefreshToken() {
  return localStorage.getItem('refresh_token');
}

function setAuth(data) {
  if (data.access_token) localStorage.setItem('access_token', data.access_token);
  if (data.refresh_token) localStorage.setItem('refresh_token', data.refresh_token);
  if (data.user) localStorage.setItem('user', JSON.stringify(data.user));
}

function clearAuth() {
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
  localStorage.removeItem('user');
}

function getUser() {
  try {
    return JSON.parse(localStorage.getItem('user') || 'null');
  } catch {
    return null;
  }
}

async function api(path, options = {}) {
  const url = `${API_BASE}${path}`;
  const headers = {
    'Content-Type': 'application/json',
    ...options.headers,
  };
  const token = getToken();
  if (token) headers['Authorization'] = `Bearer ${token}`;

  const res = await fetch(url, { ...options, headers });
  if (res.status === 401) {
    clearAuth();
    window.location.href = 'login.html';
    throw new Error('انتهت الجلسة');
  }
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: res.statusText }));
    throw new Error(err.detail || 'خطأ في الطلب');
  }
  return res.json();
}

async function login(email, password) {
  const data = await api('/auth/login', {
    method: 'POST',
    body: JSON.stringify({ email, password }),
  });
  setAuth(data);
  return data.user;
}

async function logout() {
  clearAuth();
  window.location.href = 'login.html';
}

async function fetchDashboard() {
  return api('/dashboard');
}

async function fetchTasks() {
  return api('/tasks');
}

async function createTask(data) {
  return api('/tasks', {
    method: 'POST',
    body: JSON.stringify(data),
  });
}

async function fetchContracts() {
  return api('/contracts');
}

async function fetchTeams() {
  return api('/teams');
}

async function fetchMe() {
  return api('/auth/me');
}
