const API_URL = 'http://localhost:8000';

// Modals
function openModal(modalId) {
    document.getElementById(modalId).classList.add('active');
}

function closeModal(modalId) {
    document.getElementById(modalId).classList.remove('active');
    // Clear forms when closing
    const form = document.querySelector(`#${modalId} form`);
    if(form) form.reset();
    
    // Reset hidden ID inputs and titles
    document.querySelectorAll('input[type="hidden"]').forEach(el => el.value = '');
    const title = document.querySelector(`#${modalId} .modal-header h2`);
    if(title) {
        if(title.id.includes('patient')) title.innerText = 'Add New Patient';
        if(title.id.includes('doctor')) title.innerText = 'Add New Doctor';
        if(title.id.includes('appointment')) title.innerText = 'Book Appointment';
        if(title.id.includes('billing')) title.innerText = 'Create New Bill';
    }
}

// Global fetch wrapper
async function apiCall(endpoint, method = 'GET', body = null) {
    const options = {
        method,
        headers: {
            'Content-Type': 'application/json'
        }
    };
    if (body) {
        options.body = JSON.stringify(body);
    }
    try {
        const response = await fetch(`${API_URL}${endpoint}`, options);
        if (!response.ok) throw new Error('API Request Failed');
        return await response.json();
    } catch (error) {
        console.error(error);
        alert('An error occurred while connecting to the backend. Please ensure the server is running on http://localhost:8000. Error: ' + error.message);
    }
}

// DASHBOARD
async function fetchDashboardStats() {
    const patients = await apiCall('/patients/') || [];
    const doctors = await apiCall('/doctors/') || [];
    const appointments = await apiCall('/appointments/') || [];
    const billings = await apiCall('/billings/') || [];

    if(document.getElementById('patient-count')) {
        document.getElementById('patient-count').innerText = patients.length || '0';
        document.getElementById('doctor-count').innerText = doctors.length || '0';
        document.getElementById('appointment-count').innerText = appointments.length || '0';
        document.getElementById('billing-count').innerText = billings.length || '0';
    }

    const tbody = document.querySelector('#recent-appointments-table tbody');
    if(tbody && appointments) {
        tbody.innerHTML = '';
        appointments.slice(0, 5).forEach(app => {
            tbody.innerHTML += `
                <tr>
                    <td>#${app.appointment_id}</td>
                    <td>Patient ID: ${app.patient_id}</td>
                    <td>Doctor ID: ${app.doctor_id}</td>
                    <td>${app.date}</td>
                    <td><span class="badge badge-${app.status === 'Completed' ? 'success' : (app.status === 'Cancelled' ? 'danger' : 'warning')}">${app.status}</span></td>
                </tr>
            `;
        });
    }
}

// PATIENTS
async function fetchPatients() {
    const patients = await apiCall('/patients/') || [];
    const tbody = document.querySelector('#patients-table tbody');
    if (!tbody) return;
    tbody.innerHTML = '';
    patients.forEach(p => {
        tbody.innerHTML += `
            <tr>
                <td>P-${p.patient_id}</td>
                <td><strong>${p.name}</strong></td>
                <td>${p.age}</td>
                <td>${p.gender}</td>
                <td>${p.phone}</td>
                <td>${p.address}</td>
                <td>
                    <button class="btn-icon btn-edit" onclick="editPatient('${p.patient_id}')"><i class="fa-solid fa-pen"></i></button>
                    <button class="btn-icon btn-delete" onclick="deletePatient('${p.patient_id}')"><i class="fa-solid fa-trash"></i></button>
                </td>
            </tr>
        `;
    });
}

async function savePatient() {
    const id = document.getElementById('patientId').value;
    const body = {
        name: document.getElementById('patientName').value,
        age: parseInt(document.getElementById('patientAge').value),
        gender: document.getElementById('patientGender').value,
        phone: document.getElementById('patientPhone').value,
        address: document.getElementById('patientAddress').value
    };

    if (id) {
        await apiCall(`/patients/${id}`, 'PUT', body);
    } else {
        await apiCall('/patients/', 'POST', body);
    }
    
    closeModal('patientModal');
    fetchPatients();
}

async function editPatient(id) {
    const p = await apiCall(`/patients/${id}`);
    document.getElementById('patientId').value = p.patient_id;
    document.getElementById('patientName').value = p.name;
    document.getElementById('patientAge').value = p.age;
    document.getElementById('patientGender').value = p.gender;
    document.getElementById('patientPhone').value = p.phone;
    document.getElementById('patientAddress').value = p.address;
    document.getElementById('patientModalTitle').innerText = 'Edit Patient';
    openModal('patientModal');
}

async function deletePatient(id) {
    if (confirm('Are you sure you want to delete this patient?')) {
        await apiCall(`/patients/${id}`, 'DELETE');
        fetchPatients();
    }
}

// DOCTORS
async function fetchDoctors() {
    const doctors = await apiCall('/doctors/') || [];
    const tbody = document.querySelector('#doctors-table tbody');
    if (!tbody) return;
    tbody.innerHTML = '';
    doctors.forEach(d => {
        tbody.innerHTML += `
            <tr>
                <td>D-${d.doctor_id}</td>
                <td><strong>Dr. ${d.name}</strong></td>
                <td>${d.specialization}</td>
                <td>${d.phone}</td>
                <td>${d.experience} Years</td>
                <td>
                    <button class="btn-icon btn-edit" onclick="editDoctor('${d.doctor_id}')"><i class="fa-solid fa-pen"></i></button>
                    <button class="btn-icon btn-delete" onclick="deleteDoctor('${d.doctor_id}')"><i class="fa-solid fa-trash"></i></button>
                </td>
            </tr>
        `;
    });
}

async function saveDoctor() {
    const id = document.getElementById('doctorId').value;
    const body = {
        name: document.getElementById('doctorName').value,
        specialization: document.getElementById('doctorSpecialization').value,
        phone: document.getElementById('doctorPhone').value,
        experience: parseInt(document.getElementById('doctorExperience').value)
    };

    if (id) {
        await apiCall(`/doctors/${id}`, 'PUT', body);
    } else {
        await apiCall('/doctors/', 'POST', body);
    }
    
    closeModal('doctorModal');
    fetchDoctors();
}

async function editDoctor(id) {
    const d = await apiCall(`/doctors/${id}`);
    document.getElementById('doctorId').value = d.doctor_id;
    document.getElementById('doctorName').value = d.name;
    document.getElementById('doctorSpecialization').value = d.specialization;
    document.getElementById('doctorPhone').value = d.phone;
    document.getElementById('doctorExperience').value = d.experience;
    document.getElementById('doctorModalTitle').innerText = 'Edit Doctor';
    openModal('doctorModal');
}

async function deleteDoctor(id) {
    if (confirm('Are you sure you want to delete this doctor?')) {
        await apiCall(`/doctors/${id}`, 'DELETE');
        fetchDoctors();
    }
}

// APPOINTMENTS
async function fetchAppointments() {
    const appointments = await apiCall('/appointments/') || [];
    const patients = await apiCall('/patients/') || [];
    const doctors = await apiCall('/doctors/') || [];
    
    const tbody = document.querySelector('#appointments-table tbody');
    if (!tbody) return;
    tbody.innerHTML = '';
    
    // Create maps for quick lookup
    const pMap = {}; patients.forEach(p => pMap[p.patient_id] = p.name);
    const dMap = {}; doctors.forEach(d => dMap[d.doctor_id] = d.name);

    appointments.forEach(a => {
        tbody.innerHTML += `
            <tr>
                <td>#${a.appointment_id}</td>
                <td>${pMap[a.patient_id] || a.patient_id}</td>
                <td>Dr. ${dMap[a.doctor_id] || a.doctor_id}</td>
                <td>${a.date}</td>
                <td>${a.time}</td>
                <td><span class="badge badge-${a.status === 'Completed' ? 'success' : (a.status === 'Cancelled' ? 'danger' : 'warning')}">${a.status}</span></td>
                <td>
                    <button class="btn-icon btn-edit" onclick="editAppointment('${a.appointment_id}')"><i class="fa-solid fa-pen"></i></button>
                    <button class="btn-icon btn-delete" onclick="deleteAppointment('${a.appointment_id}')"><i class="fa-solid fa-trash"></i></button>
                </td>
            </tr>
        `;
    });
}

async function fetchDropdownData() {
    const pSelect = document.getElementById('appointmentPatient');
    const dSelect = document.getElementById('appointmentDoctor');
    if(pSelect && dSelect) {
        const patients = await apiCall('/patients/') || [];
        const doctors = await apiCall('/doctors/') || [];
        
        pSelect.innerHTML = patients.map(p => `<option value="${p.patient_id}">${p.name} (ID: P-${p.patient_id})</option>`).join('');
        dSelect.innerHTML = doctors.map(d => `<option value="${d.doctor_id}">Dr. ${d.name} (${d.specialization})</option>`).join('');
    }
}

async function saveAppointment() {
    const id = document.getElementById('appointmentId').value;
    // ensure seconds format HH:MM:SS
    let timeVal = document.getElementById('appointmentTime').value;
    if(timeVal.length === 5) timeVal += ':00';
    
    const body = {
        patient_id: document.getElementById('appointmentPatient').value,
        doctor_id: document.getElementById('appointmentDoctor').value,
        date: document.getElementById('appointmentDate').value,
        time: timeVal,
        status: document.getElementById('appointmentStatus').value
    };

    if (id) {
        await apiCall(`/appointments/${id}`, 'PUT', body);
    } else {
        await apiCall('/appointments/', 'POST', body);
    }
    
    closeModal('appointmentModal');
    fetchAppointments();
}

async function editAppointment(id) {
    await fetchDropdownData();
    const a = await apiCall(`/appointments/${id}`);
    document.getElementById('appointmentId').value = a.appointment_id;
    document.getElementById('appointmentPatient').value = a.patient_id;
    document.getElementById('appointmentDoctor').value = a.doctor_id;
    document.getElementById('appointmentDate').value = a.date;
    document.getElementById('appointmentTime').value = a.time.substring(0,5);
    document.getElementById('appointmentStatus').value = a.status;
    document.getElementById('appointmentModalTitle').innerText = 'Edit Appointment';
    openModal('appointmentModal');
}

async function deleteAppointment(id) {
    if (confirm('Are you sure you want to delete this appointment?')) {
        await apiCall(`/appointments/${id}`, 'DELETE');
        fetchAppointments();
    }
}

// BILLING
async function fetchBillings() {
    const billings = await apiCall('/billings/') || [];
    const patients = await apiCall('/patients/') || [];
    
    const tbody = document.querySelector('#billings-table tbody');
    if (!tbody) return;
    tbody.innerHTML = '';
    
    const pMap = {}; patients.forEach(p => pMap[p.patient_id] = p.name);

    billings.forEach(b => {
        tbody.innerHTML += `
            <tr>
                <td>B-${b.bill_id}</td>
                <td>${pMap[b.patient_id] || b.patient_id}</td>
                <td><strong>$${b.amount.toFixed(2)}</strong></td>
                <td>${b.date}</td>
                <td><span class="badge badge-${b.payment_status === 'Paid' ? 'success' : (b.payment_status === 'Cancelled' ? 'danger' : 'warning')}">${b.payment_status}</span></td>
                <td>
                    <button class="btn-icon btn-edit" onclick="editBilling('${b.bill_id}')"><i class="fa-solid fa-pen"></i></button>
                    <button class="btn-icon btn-delete" onclick="deleteBilling('${b.bill_id}')"><i class="fa-solid fa-trash"></i></button>
                </td>
            </tr>
        `;
    });
}

async function fetchBillingDropdownData() {
    const pSelect = document.getElementById('billingPatient');
    if(pSelect) {
        const patients = await apiCall('/patients/') || [];
        pSelect.innerHTML = patients.map(p => `<option value="${p.patient_id}">${p.name} (ID: P-${p.patient_id})</option>`).join('');
    }
}

async function saveBilling() {
    const id = document.getElementById('billId').value;
    const body = {
        patient_id: document.getElementById('billingPatient').value,
        amount: parseFloat(document.getElementById('billingAmount').value),
        payment_status: document.getElementById('billingStatus').value,
        date: document.getElementById('billingDate').value
    };

    if (id) {
        await apiCall(`/billings/${id}`, 'PUT', body);
    } else {
        await apiCall('/billings/', 'POST', body);
    }
    
    closeModal('billingModal');
    fetchBillings();
}

async function editBilling(id) {
    await fetchBillingDropdownData();
    const b = await apiCall(`/billings/${id}`);
    document.getElementById('billId').value = b.bill_id;
    document.getElementById('billingPatient').value = b.patient_id;
    document.getElementById('billingAmount').value = b.amount;
    document.getElementById('billingStatus').value = b.payment_status;
    document.getElementById('billingDate').value = b.date;
    document.getElementById('billingModalTitle').innerText = 'Edit Bill';
    openModal('billingModal');
}

async function deleteBilling(id) {
    if (confirm('Are you sure you want to delete this bill?')) {
        await apiCall(`/billings/${id}`, 'DELETE');
        fetchBillings();
    }
}
