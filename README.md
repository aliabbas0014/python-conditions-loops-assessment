
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#080d19">
<title>Python Conditions & Loops Suite</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">

<style>
:root {
    --bg:#080d19;
    --surface:#111c2d;
    --surface2:#172438;
    --border:rgba(255,255,255,.09);
    --text:#f1f5f9;
    --muted:#94a3b8;
    --blue:#38bdf8;
    --green:#34d399;
    --purple:#a78bfa;
    --red:#fb7185;
}

* { margin:0; padding:0; box-sizing:border-box; }

html { scroll-behavior:smooth; }

body {
    background:var(--bg);
    color:var(--text);
    font-family:'DM Sans',sans-serif;
    overflow-x:hidden;
}

body::before, body::after {
    content:"";
    position:fixed;
    width:420px;
    height:420px;
    filter:blur(160px);
    opacity:.12;
    border-radius:50%;
    pointer-events:none;
    z-index:-1;
}

body::before {
    background:#2563eb;
    top:-180px;
    left:-130px;
}

body::after {
    background:#059669;
    bottom:-180px;
    right:-130px;
}

.container {
    width:min(1080px,92%);
    margin:auto;
}

/* NAVIGATION */

nav {
    position:sticky;
    top:0;
    z-index:10;
    background:rgba(8,13,25,.85);
    backdrop-filter:blur(15px);
    border-bottom:1px solid var(--border);
}

.nav-inner {
    min-height:72px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:15px;
}

.brand {
    display:flex;
    align-items:center;
    gap:11px;
    font-family:'Space Grotesk',sans-serif;
    font-weight:700;
    font-size:16px;
}

.brand-icon {
    height:39px;
    width:39px;
    display:grid;
    place-items:center;
    border-radius:12px;
    background:linear-gradient(135deg,#2563eb,#06b6d4);
    font-size:20px;
}

.tag {
    color:var(--blue);
    border:1px solid rgba(56,189,248,.25);
    background:rgba(56,189,248,.08);
    border-radius:30px;
    padding:7px 12px;
    font-size:10px;
    font-weight:800;
    letter-spacing:1px;
}

/* HERO */

.hero {
    text-align:center;
    padding:88px 0 65px;
    animation:fadeUp .8s ease both;
}

.eyebrow {
    display:inline-flex;
    gap:9px;
    align-items:center;
    padding:8px 15px;
    border:1px solid var(--border);
    background:rgba(255,255,255,.04);
    border-radius:30px;
    color:#cbd5e1;
    font-size:12px;
    margin-bottom:25px;
}

.dot {
    height:7px;
    width:7px;
    border-radius:50%;
    background:var(--green);
    box-shadow:0 0 12px var(--green);
}

h1 {
    font-family:'Space Grotesk',sans-serif;
    font-size:clamp(38px,6vw,66px);
    line-height:1.08;
    letter-spacing:-2px;
    max-width:850px;
    margin:auto;
}

.gradient {
    background:linear-gradient(90deg,#38bdf8,#818cf8,#34d399);
    -webkit-background-clip:text;
    background-clip:text;
    color:transparent;
}

.hero p {
    max-width:650px;
    margin:20px auto 0;
    color:var(--muted);
    font-size:14px;
    line-height:1.8;
}

.hero-actions {
    display:flex;
    justify-content:center;
    gap:12px;
    flex-wrap:wrap;
    margin-top:28px;
}

.btn {
    border:1px solid var(--border);
    border-radius:9px;
    padding:12px 19px;
    color:white;
    text-decoration:none;
    font-size:12px;
    font-weight:700;
    transition:.25s;
}

.btn-primary {
    background:linear-gradient(135deg,#2563eb,#0891b2);
    border:0;
}

.btn:hover {
    transform:translateY(-3px);
    filter:brightness(1.15);
}

/* SECTIONS */

.section-heading {
    margin:35px 0 20px;
}

.section-heading h2 {
    font-family:'Space Grotesk',sans-serif;
    font-size:24px;
}

.section-heading p {
    color:var(--muted);
    font-size:13px;
    margin-top:7px;
}

/* MODULE CARDS */

.module-grid {
    display:grid;
    grid-template-columns:repeat(2,1fr);
    gap:18px;
}

.module-card {
    background:linear-gradient(145deg,#142239,#0e1829);
    border:1px solid var(--border);
    border-radius:17px;
    padding:25px;
    position:relative;
    overflow:hidden;
    transition:.3s;
}

.module-card:hover {
    transform:translateY(-5px);
    border-color:rgba(56,189,248,.4);
}

.module-top {
    display:flex;
    align-items:center;
    justify-content:space-between;
}

.module-icon {
    width:48px;
    height:48px;
    display:grid;
    place-items:center;
    background:rgba(56,189,248,.12);
    border-radius:13px;
    font-size:23px;
}

.module-number {
    color:var(--blue);
    font-size:10px;
    font-weight:800;
    letter-spacing:1px;
}

.module-card h3 {
    font-family:'Space Grotesk',sans-serif;
    font-size:21px;
    margin-top:22px;
}

.module-card p {
    color:var(--muted);
    font-size:13px;
    line-height:1.7;
    margin-top:9px;
    min-height:45px;
}

.chips {
    display:flex;
    flex-wrap:wrap;
    gap:7px;
    margin:17px 0 20px;
}

.chip {
    padding:6px 9px;
    border:1px solid var(--border);
    border-radius:7px;
    color:#cbd5e1;
    font-size:10px;
}

.card-btn {
    width:100%;
    padding:11px;
    color:white;
    background:rgba(255,255,255,.05);
    border:1px solid var(--border);
    border-radius:8px;
    font-weight:700;
    font-size:12px;
    transition:.2s;
}

.card-btn:hover {
    border-color:var(--blue);
    background:rgba(56,189,248,.12);
}

/* PLAYGROUND */

.playground {
    margin-top:55px;
    background:rgba(17,28,45,.92);
    border:1px solid var(--border);
    border-radius:18px;
    padding:25px;
}

.playground-header {
    display:flex;
    align-items:center;
    justify-content:space-between;
    flex-wrap:wrap;
    gap:12px;
    margin-bottom:22px;
}

.playground-header h2 {
    font-family:'Space Grotesk',sans-serif;
    font-size:21px;
}

.live {
    color:var(--green);
    font-size:11px;
    font-weight:800;
}

.stats {
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:12px;
}

.stat {
    background:var(--surface2);
    border:1px solid var(--border);
    padding:18px;
    border-radius:11px;
}

.stat span {
    color:var(--muted);
    font-size:11px;
}

.stat strong {
    display:block;
    font-family:'Space Grotesk',sans-serif;
    font-size:24px;
    margin-top:8px;
}

.panels {
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:17px;
    margin-top:19px;
}

.panel {
    background:var(--surface);
    border:1px solid var(--border);
    border-radius:14px;
    padding:21px;
    min-width:0;
}

.panel h3 {
    font-family:'Space Grotesk',sans-serif;
    font-size:17px;
}

.panel-desc {
    color:var(--muted);
    font-size:11px;
    margin:7px 0 18px;
}

.form-group {
    margin-bottom:13px;
}

.form-group label {
    display:block;
    color:#cbd5e1;
    font-size:11px;
    margin-bottom:7px;
}

.form-group input,
.form-group select {
    width:100%;
    padding:11px;
    background:#0a1322;
    color:white;
    border:1px solid var(--border);
    border-radius:8px;
    outline:none;
    font-size:12px;
}

.form-group input:focus,
.form-group select:focus {
    border-color:var(--blue);
}

.action {
    width:100%;
    border:0;
    border-radius:8px;
    padding:12px;
    color:white;
    font-size:12px;
    font-weight:800;
    background:linear-gradient(135deg,#2563eb,#0891b2);
    transition:.2s;
}

.action:hover {
    filter:brightness(1.15);
    transform:translateY(-2px);
}

.action.green {
    background:linear-gradient(135deg,#059669,#0d9488);
}

.result {
    background:#0a1322;
    border:1px solid var(--border);
    border-radius:9px;
    padding:14px;
    min-height:65px;
    margin-top:14px;
    font-size:12px;
    color:#cbd5e1;
    line-height:1.8;
    overflow-wrap:anywhere;
}

.success { color:var(--green); font-weight:800; }
.warning { color:#fbbf24; font-weight:800; }
.danger { color:var(--red); font-weight:800; }

.small-actions {
    display:flex;
    gap:8px;
    margin-top:10px;
}

.small-actions button {
    flex:1;
    border:1px solid var(--border);
    background:rgba(255,255,255,.04);
    color:#cbd5e1;
    border-radius:7px;
    padding:8px;
    font-size:10px;
}

/* INVENTORY TABLE */

.table-wrap {
    overflow-x:auto;
    margin-top:14px;
}

table {
    border-collapse:collapse;
    width:100%;
    font-size:11px;
    min-width:350px;
}

th,td {
    text-align:left;
    padding:10px 8px;
    border-bottom:1px solid var(--border);
}

th {
    color:var(--muted);
    font-weight:600;
}

td { color:#e2e8f0; }

.stock-low { color:#fbbf24; }
.stock-ok { color:var(--green); }

/* CONCEPTS */

.concepts {
    margin:60px 0;
    text-align:center;
}

.concepts h2 {
    font-family:'Space Grotesk',sans-serif;
    font-size:24px;
}

.concepts p {
    color:var(--muted);
    font-size:12px;
    margin-top:8px;
}

.concept-list {
    display:flex;
    justify-content:center;
    flex-wrap:wrap;
    gap:9px;
    margin-top:22px;
}

.concept {
    padding:10px 15px;
    border:1px solid var(--border);
    background:var(--surface);
    border-radius:8px;
    font-size:11px;
    color:#cbd5e1;
}

/* FOOTER */

footer {
    border-top:1px solid var(--border);
    padding:27px 0;
    text-align:center;
    color:var(--muted);
    font-size:11px;
    line-height:2;
}

footer strong { color:#e2e8f0; }

@keyframes fadeUp {
    from { opacity:0; transform:translateY(22px); }
    to { opacity:1; transform:translateY(0); }
}

@media(max-width:700px) {
    .hero { padding:65px 0 45px; }
    .module-grid,.panels { grid-template-columns:1fr; }
    .stats { grid-template-columns:1fr; }
    .stat { display:flex; justify-content:space-between; align-items:center; }
    .stat strong { margin:0; }
    .playground { padding:15px; }
    .module-card { padding:20px; }
    h1 { letter-spacing:-1px; }
}
</style>
</head>

<body>

<nav>
    <div class="container nav-inner">
        <div class="brand">
            <div class="brand-icon">⌘</div>
            <span>Python Conditions & Loops</span>
        </div>
        <span class="tag">ASSESSMENT 01</span>
    </div>
</nav>

<header class="container hero">
    <div class="eyebrow">
        <span class="dot"></span>
        Python Programming Project
    </div>

    <h1>
        Learn Python Through
        <span class="gradient">Practical Applications</span>
    </h1>

    <p>
        Two practical console-based applications demonstrating
        conditional statements, loops, input validation, and
        real-world calculations using Python.
    </p>

    <div class="hero-actions">
        <a href="#modules" class="btn btn-primary">Explore Modules ↗</a>
        <a href="#playground" class="btn">Try Interactive Demo ↓</a>
    </div>
</header>

<main class="container">

    <section id="modules">
        <div class="section-heading">
            <h2>Project Modules</h2>
            <p>Two Python applications built around practical problem-solving.</p>
        </div>

        <div class="module-grid">

            <article class="module-card">
                <div class="module-top">
                    <div class="module-icon">🎓</div>
                    <span class="module-number">MODULE 01</span>
                </div>

                <h3>Student Scholarship System</h3>

                <p>
                    Evaluate student scholarship eligibility using
                    academic marks, attendance, and monthly family income.
                </p>

                <div class="chips">
                    <span class="chip">If / Elif / Else</span>
                    <span class="chip">Input Validation</span>
                    <span class="chip">Logical Operators</span>
                </div>

                <button class="card-btn"
                    onclick="document.getElementById('scholarshipPanel').scrollIntoView({behavior:'smooth'})">
                    Try Scholarship Calculator →
                </button>
            </article>

            <article class="module-card">
                <div class="module-top">
                    <div class="module-icon">💊</div>
                    <span class="module-number">MODULE 02</span>
                </div>

                <h3>Pharmacy Inventory System</h3>

                <p>
                    Manage medicine stock, process sales, calculate
                    revenue, and identify medicines requiring restocking.
                </p>

                <div class="chips">
                    <span class="chip">For Loops</span>
                    <span class="chip">While Loops</span>
                    <span class="chip">Counters & Accumulators</span>
                </div>

                <button class="card-btn"
                    onclick="document.getElementById('pharmacyPanel').scrollIntoView({behavior:'smooth'})">
                    Try Inventory Demo →
                </button>
            </article>

        </div>
    </section>

    <section class="playground" id="playground">

        <div class="playground-header">
            <h2>Interactive Project Playground</h2>
            <span class="live">● LIVE PREVIEW</span>
        </div>

        <div class="stats">
            <div class="stat">
                <span>Scholarship Checks</span>
                <strong id="checkCount">0</strong>
            </div>

            <div class="stat">
                <span>Medicines Processed</span>
                <strong id="medicineCount">0</strong>
            </div>

            <div class="stat">
                <span>Demo Sales Revenue</span>
                <strong id="revenue">Rs. 0</strong>
            </div>
        </div>

        <div class="panels">

            <!-- SCHOLARSHIP CALCULATOR -->

            <section class="panel" id="scholarshipPanel">
                <h3>🎓 Scholarship Calculator</h3>
                <p class="panel-desc">
                    Enter student details to check scholarship eligibility.
                </p>

                <form id="scholarshipForm">

                    <div class="form-group">
                        <label for="studentName">Student Name</label>
                        <input id="studentName" type="text"
                            placeholder="Enter student name" required>
                    </div>

                    <div class="form-group">
                        <label for="marks">Marks Percentage</label>
                        <input id="marks" type="number"
                            min="0" max="100" step="0.01"
                            placeholder="e.g. 95" required>
                    </div>

                    <div class="form-group">
                        <label for="attendance">Attendance Percentage</label>
                        <input id="attendance" type="number"
                            min="0" max="100" step="0.01"
                            placeholder="e.g. 90" required>
                    </div>

                    <div class="form-group">
                        <label for="income">Monthly Family Income (PKR)</label>
                        <input id="income" type="number"
                            min="0" step="0.01"
                            placeholder="e.g. 40000" required>
                    </div>

                    <button class="action" type="submit">
                        Check Scholarship Eligibility
                    </button>
                </form>

                <div class="result" id="scholarshipResult" aria-live="polite">
                    Enter student information to see the eligibility report.
                </div>

                <div class="small-actions">
                    <button type="button" onclick="loadScholarshipSample()">Load Sample</button>
                    <button type="button" onclick="resetScholarship()">Reset</button>
                </div>
            </section>

            <!-- PHARMACY INVENTORY -->

            <section class="panel" id="pharmacyPanel">
                <h3>💊 Pharmacy Inventory</h3>
                <p class="panel-desc">
                    Add medicines and simulate sales with stock verification.
                </p>

                <form id="pharmacyForm">

                    <div class="form-group">
                        <label for="medicineName">Medicine Name</label>
                        <input id="medicineName" type="text"
                            placeholder="e.g. Panadol" required>
                    </div>

                    <div class="form-group">
                        <label for="stock">Available Stock</label>
                        <input id="stock" type="number"
                            min="0" step="1"
                            placeholder="e.g. 20" required>
                    </div>

                    <div class="form-group">
                        <label for="price">Price Per Unit (PKR)</label>
                        <input id="price" type="number"
                            min="0.01" step="0.01"
                            placeholder="e.g. 50" required>
                    </div>

                    <div class="form-group">
                        <label for="quantity">Quantity Sold</label>
                        <input id="quantity" type="number"
                            min="0" step="1"
                            placeholder="e.g. 5" required>
                    </div>

                    <button class="action green" type="submit">
                        Process Medicine Sale
                    </button>
                </form>

                <div class="result" id="pharmacyResult" aria-live="polite">
                    Enter medicine details to simulate a sale.
                </div>

                <div class="table-wrap">
                    <table>
                        <thead>
                            <tr>
                                <th>Medicine</th>
                                <th>Sold</th>
                                <th>Remaining</th>
                                <th>Sales</th>
                            </tr>
                        </thead>
                        <tbody id="inventoryBody">
                            <tr>
                                <td colspan="4">No medicines processed yet.</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <div class="small-actions">
                    <button type="button" onclick="loadPharmacySample()">Load Sample</button>
                    <button type="button" onclick="resetPharmacy()">Reset Data</button>
                </div>
            </section>

        </div>
    </section>

    <section class="concepts">
        <h2>Python Concepts Demonstrated</h2>
        <p>Fundamental programming techniques applied in practical scenarios.</p>

        <div class="concept-list">
            <span class="concept">🐍 Python 3</span>
            <span class="concept">If / Elif / Else</span>
            <span class="concept">For Loops</span>
            <span class="concept">While Loops</span>
            <span class="concept">Range Function</span>
            <span class="concept">Lists</span>
            <span class="concept">Try / Except</span>
            <span class="concept">Input Validation</span>
            <span class="concept">Counters</span>
            <span class="concept">Accumulators</span>
        </div>
    </section>

</main>

<footer>
    <div class="container">
        <strong>Python Conditions & Loops Suite</strong><br>
        Assessment 01 · Student Scholarship & Pharmacy Inventory Management<br>
        Interactive project showcase · Built for learning and demonstration
    </div>
</footer>

<script>
    // DEMO STATISTICS

    let scholarshipChecks = 0;
    let medicineCount = 0;
    let totalRevenue = 0;
    let inventory = [];

    function updateStats() {
        document.getElementById("checkCount").textContent =
            scholarshipChecks;

        document.getElementById("medicineCount").textContent =
            medicineCount;

        document.getElementById("revenue").textContent =
            "Rs. " + totalRevenue.toLocaleString("en-PK", {
                maximumFractionDigits: 2
            });
    }

    function escapeHTML(value) {
        return String(value).replace(/[&<>"']/g, char => ({
            "&": "&amp;",
            "<": "&lt;",
            ">": "&gt;",
            '"': "&quot;",
            "'": "&#39;"
        })[char]);
    }

    // SCHOLARSHIP ELIGIBILITY

    document.getElementById("scholarshipForm")
        .addEventListener("submit", function(event) {

        event.preventDefault();

        const name = document.getElementById("studentName").value.trim();
        const marks = Number(document.getElementById("marks").value);
        const attendance = Number(document.getElementById("attendance").value);
        const income = Number(document.getElementById("income").value);

        const result = document.getElementById("scholarshipResult");

        if (!name || !Number.isFinite(marks) ||
            !Number.isFinite(attendance) ||
            !Number.isFinite(income) ||
            marks < 0 || marks > 100 ||
            attendance < 0 || attendance > 100 ||
            income < 0) {

            result.innerHTML =
                '<span class="danger">Please enter valid information.</span>';
            return;
        }

        scholarshipChecks++;

        const reasons = [];

        if (marks < 80) {
            reasons.push("Marks must be 80% or above.");
        }

        if (attendance < 85) {
            reasons.push("Attendance must be 85% or above.");
        }

        if (income > 50000) {
            reasons.push("Monthly family income must be Rs. 50,000 or less.");
        }

        let html = "<strong>Student Name:</strong> " +
            escapeHTML(name) + "<br>";

        if (reasons.length === 0) {

            const category = marks >= 90
                ? "Full Scholarship"
                : "Partial Scholarship";

            html += '<span class="success">✓ Eligible</span><br>';
            html += "<strong>Scholarship Category:</strong> " + category;

        } else {

            html += '<span class="danger">✕ Not Eligible</span><br>';
            html += "<strong>Reasons:</strong><br>";

            reasons.forEach(reason => {
                html += "• " + escapeHTML(reason) + "<br>";
            });
        }

        result.innerHTML = html;
        updateStats();
    });

    function loadScholarshipSample() {
        document.getElementById("studentName").value = "Ali";
        document.getElementById("marks").value = 95;
        document.getElementById("attendance").value = 90;
        document.getElementById("income").value = 40000;
    }

    function resetScholarship() {
        document.getElementById("scholarshipForm").reset();

        document.getElementById("scholarshipResult").textContent =
            "Enter student information to see the eligibility report.";
    }

    // PHARMACY INVENTORY

    document.getElementById("pharmacyForm")
        .addEventListener("submit", function(event) {

        event.preventDefault();

        const name = document.getElementById("medicineName").value.trim();
        const stock = Number(document.getElementById("stock").value);
        const price = Number(document.getElementById("price").value);
        const quantity = Number(document.getElementById("quantity").value);

        const result = document.getElementById("pharmacyResult");

        if (!name ||
            !Number.isInteger(stock) || stock < 0 ||
            !Number.isFinite(price) || price <= 0 ||
            !Number.isInteger(quantity) || quantity < 0) {

            result.innerHTML =
                '<span class="danger">Please enter valid medicine details.</span>';
            return;
        }

        if (quantity > stock) {
            result.innerHTML =
                '<span class="danger">Insufficient stock!</span><br>' +
                "Available stock: " + stock +
                "<br>Requested quantity: " + quantity;
            return;
        }

        const remaining = stock - quantity;
        const sales = price * quantity;

        inventory.push({
            name: name,
            sold: quantity,
            remaining: remaining,
            sales: sales
        });

        medicineCount++;
        totalRevenue += sales;

        let html =
            '<span class="success">✓ Sale processed successfully!</span><br>' +
            "<strong>Medicine:</strong> " + escapeHTML(name) + "<br>" +
            "<strong>Sales Amount:</strong> Rs. " +
            sales.toLocaleString("en-PK", {maximumFractionDigits:2}) + "<br>" +
            "<strong>Remaining Stock:</strong> " + remaining + "<br>";

        if (remaining < 10) {
            html += '<span class="warning">⚠ Low stock! Restocking required.</span>';
        } else {
            html += '<span class="success">Stock level is sufficient.</span>';
        }

        result.innerHTML = html;

        updateInventoryTable();
        updateStats();
        document.getElementById("pharmacyForm").reset();
    });

    function updateInventoryTable() {
        const body = document.getElementById("inventoryBody");

        if (inventory.length === 0) {
            body.innerHTML =
                '<tr><td colspan="4">No medicines processed yet.</td></tr>';
            return;
        }

        body.innerHTML = inventory.map(item => `
            <tr>
                <td>${escapeHTML(item.name)}</td>
                <td>${item.sold}</td>
                <td class="${item.remaining < 10 ? 'stock-low' : 'stock-ok'}">
                    ${item.remaining}
                </td>
                <td>Rs. ${item.sales.toLocaleString("en-PK", {
                    maximumFractionDigits: 2
                })}</td>
            </tr>
        `).join("");
    }

    function loadPharmacySample() {
        document.getElementById("medicineName").value = "Panadol";
        document.getElementById("stock").value = 20;
        document.getElementById("price").value = 50;
        document.getElementById("quantity").value = 5;
    }

    function resetPharmacy() {
        inventory = [];
        medicineCount = 0;
        totalRevenue = 0;

        document.getElementById("pharmacyForm").reset();

        document.getElementById("pharmacyResult").textContent =
            "Enter medicine details to simulate a sale.";

        updateInventoryTable();
        updateStats();
    }
</script>

</body>
</html>
