// Function to load and display inventory
async function loadInventory() {
    const response = await fetch('/api/products');
    const products = await response.json();
    
    const tbody = document.getElementById('inventory-body');
    tbody.innerHTML = '';
    
    products.forEach(product => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${product.name}</td>
            <td>${product.category}</td>
            <td>${product.quantity}</td>
            <td>${product.expiry_date || 'N/A'}</td>
            <td>
                <button onclick="editProduct('${product.barcode}')">Edit</button>
                <button onclick="updateQuantity('${product.barcode}')">Update Qty</button>
            </td>
        `;
        tbody.appendChild(row);
    });
}

// Navigation functions
function showInventory() {
    document.getElementById('inventory-section').classList.remove('hidden');
    document.getElementById('scanner-section').classList.add('hidden');
    loadInventory();
}

function showScanner() {
    document.getElementById('scanner-section').classList.remove('hidden');
    document.getElementById('inventory-section').classList.add('hidden');
}

// Load inventory when page loads
document.addEventListener('DOMContentLoaded', loadInventory);
