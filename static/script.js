document.getElementById('appointment-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    let clientName = document.getElementById('client_name').value;
    let petName = document.getElementById('pet_name').value;
    let date = document.getElementById('date').value;
    let reason = document.getElementById('reason').value;
    
    let appointment = {
        clientName,
        petName,
        date,
        reason
    };
    
    let appointments = localStorage.getItem('appointments') ? JSON.parse(localStorage.getItem('appointments')) : [];
    appointments.push(appointment);
    localStorage.setItem('appointments', JSON.stringify(appointments));
    
    document.getElementById('appointment-form').reset();
    displayAppointments();
});

function displayAppointments() {
    let appointments = localStorage.getItem('appointments') ? JSON.parse(localStorage.getItem('appointments')) : [];
    let appointmentsList = document.getElementById('appointments-list');
    appointmentsList.innerHTML = '';
    
    appointments.forEach(appointment => {
        let li = document.createElement('li');
        li.innerHTML = `${appointment.clientName} - ${appointment.petName} on ${appointment.date}: ${appointment.reason}`;
        appointmentsList.appendChild(li);
    });
}

document.addEventListener('DOMContentLoaded', displayAppointments);
