<!DOCTYPE html>
<html lang="nl">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Politie API – Officiële Dataomgeving</title>

    <!-- Bootstrap CSS CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styling -->
    <style>
        body {
            background-color: #f4f5f7;
        }

        .header-bg {
            background-color: #0a2b63;
        }

        .border-police {
            border-left: 5px solid #0a2b63 !important;
        }
    </style>
</head>

<body>

    <!-- Header -->
    <header class="header-bg text-white py-4 mb-5 shadow">
        <div class="container d-flex justify-content-between align-items-center">
            <h1 class="m-0 fw-bold">Politie API</h1>
            <nav class="d-none d-md-flex gap-4 fs-5">
                <a href="#" class="text-white text-decoration-none">Home</a>
                <a href="#" class="text-white text-decoration-none">Documentatie</a>
                <a href="#" class="text-white text-decoration-none">Endpoints</a>
                <a href="#" class="text-white text-decoration-none">Contact</a>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="container">
        <div class="bg-white rounded shadow p-5 mb-5">
            <h2 class="fw-bold text-primary mb-3">Officiële API voor Casusinformatie</h2>
            <p class="fs-5">
                Welkom bij de centrale dataomgeving van de Nederlandse Politie.
                Via deze API krijgen geautoriseerde gebruikers toegang tot casusdata, getuigenverklaringen,
                statusupdates en andere relevante informatie.
            </p>

            <p class="fs-5">
                Deze API is bedoeld voor onderzoeksdoeleinden, interne dashboards en educatieve trajecten waarin gewerkt
                wordt met echte dataformaten.
            </p>

            <a href="#" class="btn btn-primary mt-3 px-4 py-2 fs-5">Lees de API Documentatie</a>
        </div>
    </section>

    <!-- Endpoints Section -->
    <section class="container mb-5">
        <h3 class="fw-bold text-primary mb-4">Voorbeeld Endpoints</h3>
        
        <div class="alert alert-info mb-4" role="alert">
            <strong>🔐 Authenticatie vereist:</strong> Alle endpoints vereisen een API key in de <code>X-API-Key</code> header.
        </div>

        <div class="row g-4">
            <div class="col-md-6">
                <div class="bg-white p-4 rounded shadow border-police">
                    <h4 class="fw-semibold mb-2">Onderzoeken Overzicht</h4>
                    <p>Haal een lijst op van alle onderzoeken.</p>
                    <pre class="bg-light p-3 rounded"><code>GET /api/investigations</code></pre>
                </div>
            </div>

            <div class="col-md-6">
                <div class="bg-white p-4 rounded shadow border-police">
                    <h4 class="fw-semibold mb-2">Onderzoek Details</h4>
                    <p>Haal details op van een specifiek onderzoek.</p>
                    <pre class="bg-light p-3 rounded"><code>GET /api/investigations/{id}</code></pre>
                </div>
            </div>

            <div class="col-md-6">
                <div class="bg-white p-4 rounded shadow border-police">
                    <h4 class="fw-semibold mb-2">Getuigen Overzicht</h4>
                    <p>Haal een lijst op van alle geregistreerde getuigen.</p>
                    <pre class="bg-light p-3 rounded"><code>GET /api/witnesses</code></pre>
                </div>
            </div>

            <div class="col-md-6">
                <div class="bg-white p-4 rounded shadow border-police">
                    <h4 class="fw-semibold mb-2">Getuige Details</h4>
                    <p>Haal details op van een specifieke getuige.</p>
                    <pre class="bg-light p-3 rounded"><code>GET /api/witnesses/{id}</code></pre>
                </div>
            </div>

            <div class="col-md-6">
                <div class="bg-white p-4 rounded shadow border-police">
                    <h4 class="fw-semibold mb-2">Personen Overzicht</h4>
                    <p>Haal een lijst op van alle geregistreerde personen.</p>
                    <pre class="bg-light p-3 rounded"><code>GET /api/people</code></pre>
                </div>
            </div>

            <div class="col-md-6">
                <div class="bg-white p-4 rounded shadow border-police">
                    <h4 class="fw-semibold mb-2">Persoon Details</h4>
                    <p>Haal details op van een specifieke persoon.</p>
                    <pre class="bg-light p-3 rounded"><code>GET /api/people/{id}</code></pre>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="header-bg text-white py-4 mt-5">
        <div class="container text-center">
            &copy; {{ date('Y') }} Politie API — Fictief educatief platform
        </div>
    </footer>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

</body>

</html>
