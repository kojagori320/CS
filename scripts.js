document.addEventListener('DOMContentLoaded', () => {
    const customerRequests = [
        { name: "Alice", email: "alice@example.com", product: "Toys", country: "USA" },
        { name: "Bob", email: "bob@example.com", product: "Books", country: "UK" },
        { name: "Charlie", email: "charlie@example.com", product: "Clothes", country: "Canada" }
    ];

    const requestPackageBtn = document.getElementById('request-package-btn');
    const intermediariesBtn = document.getElementById('intermediaries-btn');
    const customerRequestsBtn = document.getElementById('customer-requests-btn');
    const contentDiv = document.getElementById('content');

    requestPackageBtn.addEventListener('click', openRequestForm);
    intermediariesBtn.addEventListener('click', openIntermediaries);
    customerRequestsBtn.addEventListener('click', openCustomerRequests);

    function openRequestForm() {
        contentDiv.innerHTML = `
            <h3>Request a Package</h3>
            <form id="requestForm">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <label for="product">Product Description:</label>
                <textarea id="product" name="product" rows="4" required></textarea>
                
                <label for="country">Country of Purchase:</label>
                <input type="text" id="country" name="country" required>
                
                <button type="button" class="btn" id="submit-request-btn">Submit Request</button>
            </form>
            <div class="success-message" id="successMessage"></div>
        `;
        document.getElementById('submit-request-btn').addEventListener('click', submitRequest);
    }

    function openCustomerRequests() {
        contentDiv.innerHTML = `
            <h3>Customer Requests</h3>
            ${customerRequests.map(request => `
                <div class="request">
                    <p><strong>Name:</strong> ${request.name}<br>
                    <strong>Email:</strong> ${request.email}<br>
                    <strong>Product:</strong> ${request.product}<br>
                    <strong>Country:</strong> ${request.country}<br>
                    <button class="btn" onclick="connectCustomer('${request.name}', '${request.email}')">Connect</button></p>
                </div>
            `).join('')}
        `;
    }

    function openIntermediaries() {
        contentDiv.innerHTML = `
            <h3>Available Intermediaries</h3>
            <div class="intermediary">
                <p><strong>John Doe</strong> - USA<br>Phone: 123-456-7890<br>Email: john@example.com <button class="btn" onclick="connect('John Doe', '123-456-7890', 'john@example.com')">Connect</button></p>
            </div>
            <div class="intermediary">
                <p><strong>Jane Smith</strong> - UK<br>Phone: 098-765-4321<br>Email: jane@example.com <button class="btn" onclick="connect('Jane Smith', '098-765-4321', 'jane@example.com')">Connect</button></p>
            </div>
            <h3>Available Subsidiaries</h3>
            <div class="subsidiary">
                <p><strong>ABC Logistics</strong> - Canada<br>Phone: 555-123-4567<br>Email: info@abclogistics.com <button class="btn" onclick="connect('ABC Logistics', '555-123-4567', 'info@abclogistics.com')">Connect</button></p>
            </div>
            <div class="subsidiary">
                <p><strong>XYZ Shipping</strong> - Australia<br>Phone: 555-987-6543<br>Email: contact@xyzshipping.com <button class="btn" onclick="connect('XYZ Shipping', '555-987-6543', 'contact@xyzshipping.com')">Connect</button></p>
            </div>
        `;
    }

    function submitRequest() {
        const formData = {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            product: document.getElementById('product').value,
            country: document.getElementById('country').value
        };
        
        customerRequests.push(formData);
        const csvData = convertToCSV(formData);
        downloadCSV(csvData, 'customer_requests.csv');
        
        document.getElementById('successMessage').innerText = 'Request submitted and saved as CSV!';
        document.getElementById('requestForm').reset();
    }

    function connect(name, phone, email) {
        alert(`Connecting to ${name}, Phone: ${phone}, Email: ${email}`);
    }

    function connectCustomer(name, email) {
        alert(`Connecting to customer: ${name}, Email: ${email}`);
    }

    function convertToCSV(obj) {
        const keys = Object.keys(obj).join(',');
        const values = Object.values(obj).join(',');
        return `${keys}\n${values}`;
    }

    function downloadCSV(csvContent, fileName) {
        const blob = new Blob([csvContent], { type: 'text/csv' });
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = fileName;
        link.click();
    }
});
