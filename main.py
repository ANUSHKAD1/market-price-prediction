# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
# import requests

# app = FastAPI()

# API_KEY = "579b464db66ec23bdd00000171f04671ff624c5858b2534935fb7bc8"  # Replace with your actual key
# DATASET_ID = "9ef84268-d588-465a-a308-a864a43d0070"  # All India, all crops, all markets

# def fetch_all_data():
#     """Fetch all pages of data from the API."""
#     url = f"https://api.data.gov.in/resource/{DATASET_ID}"
#     all_records = []
#     offset = 0

#     while True:
#         params = {
#             "api-key": API_KEY,
#             "format": "json",
#             "limit": 100,
#             "offset": offset
#         }
#         response = requests.get(url, params=params)
#         if response.status_code != 200:
#             break

#         data = response.json()
#         records = data.get("records", [])
#         if not records:
#             break

#         all_records.extend(records)
#         offset += 100

#     return all_records

# @app.get("/raw")
# def get_raw_data():
#     records = fetch_all_data()
#     return {"total_records": len(records), "records": records}

# @app.get("/table", response_class=HTMLResponse)
# def get_table():
#     records = fetch_all_data()

#     html = """
#     <html>
#     <head>
#         <title>Market Prices Table</title>
#         <style>
#             table {border-collapse: collapse; width: 100%;}
#             th, td {border: 1px solid black; padding: 8px; text-align: left;}
#             th {background-color: #f2f2f2;}
#         </style>
#     </head>
#     <body>
#         <h2>Market Prices</h2>
#         <table>
#             <tr>
#                 <th>State</th>
#                 <th>District</th>
#                 <th>Market</th>
#                 <th>Commodity</th>
#                 <th>Variety</th>
#                 <th>Grade</th>
#                 <th>Arrival Date</th>
#                 <th>Min Price</th>
#                 <th>Max Price</th>
#                 <th>Modal Price</th>
#             </tr>
#     """

#     for rec in records:
#         html += f"""
#         <tr>
#             <td>{rec.get('state', '')}</td>
#             <td>{rec.get('district', '')}</td>
#             <td>{rec.get('market', '')}</td>
#             <td>{rec.get('commodity', '')}</td>
#             <td>{rec.get('variety', '')}</td>
#             <td>{rec.get('grade', '')}</td>
#             <td>{rec.get('arrival_date', '')}</td>
#             <td>{rec.get('min_price', '')}</td>
#             <td>{rec.get('max_price', '')}</td>
#             <td>{rec.get('modal_price', '')}</td>
#         </tr>
#         """

#     html += """
#         </table>
#     </body>
#     </html>
#     """
#     return html

# @app.get("/")
# def root():
#     return {"message": "Visit /raw for JSON data or /table for HTML table"}


from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
import requests

app = FastAPI()

API_KEY = "579b464db66ec23bdd00000171f04671ff624c5858b2534935fb7bc8"
DATASET_ID = "9ef84268-d588-465a-a308-a864a43d0070"  # All India, all crops, all markets

def fetch_all_data():
    """Fetch all pages of data from the API."""
    url = f"https://api.data.gov.in/resource/{DATASET_ID}"
    all_records = []
    offset = 0

    while True:
        params = {
            "api-key": API_KEY,
            "format": "json",
            "limit": 100,
            "offset": offset
        }
        response = requests.get(url, params=params)
        if response.status_code != 200:
            break

        data = response.json()
        records = data.get("records", [])
        if not records:
            break

        all_records.extend(records)
        offset += 100

    return all_records

@app.get("/raw")
def get_raw_data():
    records = fetch_all_data()
    return {"total_records": len(records), "records": records}

# @app.get("/table", response_class=HTMLResponse)
# def get_table(
#     state: str = Query(None),
#     district: str = Query(None),
#     market: str = Query(None),
#     commodity: str = Query(None)
# ):
#     records = fetch_all_data()

#     # Apply filters if provided
#     if state:
#         records = [r for r in records if r.get('state', '').lower() == state.lower()]
#     if district:
#         records = [r for r in records if r.get('district', '').lower() == district.lower()]
#     if market:
#         records = [r for r in records if r.get('market', '').lower() == market.lower()]
#     if commodity:
#         records = [r for r in records if r.get('commodity', '').lower() == commodity.lower()]

#     html = """
#     <html>
#     <head>
#         <title>Market Prices Table</title>
#         <style>
#             table {border-collapse: collapse; width: 100%;}
#             th, td {border: 1px solid black; padding: 8px; text-align: left;}
#             th {background-color: #f2f2f2;}
#         </style>
#     </head>
#     <body>
#         <h2>Market Prices</h2>
#         <table>
#             <tr>
#                 <th>State</th>
#                 <th>District</th>
#                 <th>Market</th>
#                 <th>Commodity</th>
#                 <th>Variety</th>
#                 <th>Grade</th>
#                 <th>Arrival Date</th>
#                 <th>Min Price</th>
#                 <th>Max Price</th>
#                 <th>Modal Price</th>
#             </tr>
#     """

#     for rec in records:
#         html += f"""
#         <tr>
#             <td>{rec.get('state', '')}</td>
#             <td>{rec.get('district', '')}</td>
#             <td>{rec.get('market', '')}</td>
#             <td>{rec.get('commodity', '')}</td>
#             <td>{rec.get('variety', '')}</td>
#             <td>{rec.get('grade', '')}</td>
#             <td>{rec.get('arrival_date', '')}</td>
#             <td>{rec.get('min_price', '')}</td>
#             <td>{rec.get('max_price', '')}</td>
#             <td>{rec.get('modal_price', '')}</td>
#         </tr>
#         """

#     html += """
#         </table>
#     </body>
#     </html>
#     """
#     return html

# @app.get("/table", response_class=HTMLResponse)
# def get_table():
#     records = fetch_all_data()

#     # Extract unique values for filters
#     states = sorted({rec.get('state', '') for rec in records if rec.get('state')})
#     districts = sorted({rec.get('district', '') for rec in records if rec.get('district')})
#     commodities = sorted({rec.get('commodity', '') for rec in records if rec.get('commodity')})

#     html = """
#     <html>
#     <head>
#         <title>Market Prices Table</title>
#         <link rel="stylesheet" 
#               href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css">
#         <style>
#             body {font-family: Arial, sans-serif; margin: 20px;}
#             select {margin-right: 10px; padding: 5px;}
#         </style>
#     </head>
#     <body>
#         <h2>Market Prices</h2>

#         <label>State: </label>
#         <select id="stateFilter">
#             <option value="">All</option>
#     """
#     for state in states:
#         html += f"<option value='{state}'>{state}</option>"
#     html += """
#         </select>

#         <label>District: </label>
#         <select id="districtFilter">
#             <option value="">All</option>
#     """
#     for dist in districts:
#         html += f"<option value='{dist}'>{dist}</option>"
#     html += """
#         </select>

#         <label>Commodity: </label>
#         <select id="commodityFilter">
#             <option value="">All</option>
#     """
#     for com in commodities:
#         html += f"<option value='{com}'>{com}</option>"
#     html += """
#         </select>

#         <table id="marketTable" class="display">
#             <thead>
#                 <tr>
#                     <th>State</th>
#                     <th>District</th>
#                     <th>Market</th>
#                     <th>Commodity</th>
#                     <th>Variety</th>
#                     <th>Grade</th>
#                     <th>Arrival Date</th>
#                     <th>Min Price</th>
#                     <th>Max Price</th>
#                     <th>Modal Price</th>
#                 </tr>
#             </thead>
#             <tbody>
#     """

#     for rec in records:
#         html += f"""
#         <tr>
#             <td>{rec.get('state', '')}</td>
#             <td>{rec.get('district', '')}</td>
#             <td>{rec.get('market', '')}</td>
#             <td>{rec.get('commodity', '')}</td>
#             <td>{rec.get('variety', '')}</td>
#             <td>{rec.get('grade', '')}</td>
#             <td>{rec.get('arrival_date', '')}</td>
#             <td>{rec.get('min_price', '')}</td>
#             <td>{rec.get('max_price', '')}</td>
#             <td>{rec.get('modal_price', '')}</td>
#         </tr>
#         """

#     html += """
#             </tbody>
#         </table>

#         <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
#         <script src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>
#         <script>
#             $(document).ready(function () {
#                 var table = $('#marketTable').DataTable();

#                 $('#stateFilter').on('change', function () {
#                     table.column(0).search(this.value).draw();
#                 });
#                 $('#districtFilter').on('change', function () {
#                     table.column(1).search(this.value).draw();
#                 });
#                 $('#commodityFilter').on('change', function () {
#                     table.column(3).search(this.value).draw();
#                 });
#             });
#         </script>
#     </body>
#     </html>
#     """

#     return html

# @app.get("/table", response_class=HTMLResponse)
# def get_table():
#     records = fetch_all_data()

#     # Extract unique values for filters
#     states = sorted({rec.get('state', '') for rec in records if rec.get('state')})
#     districts = sorted({rec.get('district', '') for rec in records if rec.get('district')})
#     commodities = sorted({rec.get('commodity', '') for rec in records if rec.get('commodity')})

#     html = """
#     <html>
#     <head>
#         <title>Market Prices Table</title>
#         <link rel="stylesheet" 
#               href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css">
#         <style>
#             body {
#                 font-family: 'Segoe UI', Tahoma, sans-serif;
#                 margin: 20px;
#                 background: linear-gradient(135deg, #fbc2eb, #a6c1ee, #fbc2eb);
#                 background-size: 400% 400%;
#                 animation: gradientBG 15s ease infinite;
#                 color: #333;
#             }
#             @keyframes gradientBG {
#                 0% { background-position: 0% 50%; }
#                 50% { background-position: 100% 50%; }
#                 100% { background-position: 0% 50%; }
#             }
#             h2 {
#                 text-align: center;
#                 color: #444;
#                 text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
#             }
#             select {
#                 margin-right: 10px;
#                 padding: 5px;
#                 border-radius: 8px;
#                 border: 1px solid #ccc;
#                 box-shadow: 0 2px 5px rgba(0,0,0,0.1);
#                 background: rgba(255,255,255,0.8);
#                 backdrop-filter: blur(4px);
#             }
#             table.dataTable {
#                 border-radius: 12px;
#                 overflow: hidden;
#                 background: rgba(255,255,255,0.85);
#                 box-shadow: 0 4px 20px rgba(0,0,0,0.1);
#             }
#             table.dataTable thead {
#                 background: linear-gradient(to right, #ffecd2, #fcb69f);
#                 color: #333;
#                 font-weight: bold;
#             }
#             table.dataTable tbody tr:hover {
#                 background: rgba(255, 236, 210, 0.6);
#                 transition: background 0.3s ease;
#             }
#             label {
#                 font-weight: bold;
#                 color: #333;
#             }
#         </style>
#     </head>
#     <body>
#         <h2>Market Prices</h2>

#         <label>State: </label>
#         <select id="stateFilter">
#             <option value="">All</option>
#     """
#     for state in states:
#         html += f"<option value='{state}'>{state}</option>"
#     html += """
#         </select>

#         <label>District: </label>
#         <select id="districtFilter">
#             <option value="">All</option>
#     """
#     for dist in districts:
#         html += f"<option value='{dist}'>{dist}</option>"
#     html += """
#         </select>

#         <label>Commodity: </label>
#         <select id="commodityFilter">
#             <option value="">All</option>
#     """
#     for com in commodities:
#         html += f"<option value='{com}'>{com}</option>"
#     html += """
#         </select>

#         <table id="marketTable" class="display" style="width:100%">
#             <thead>
#                 <tr>
#                     <th>State</th>
#                     <th>District</th>
#                     <th>Market</th>
#                     <th>Commodity</th>
#                     <th>Variety</th>
#                     <th>Grade</th>
#                     <th>Arrival Date</th>
#                     <th>Min Price</th>
#                     <th>Max Price</th>
#                     <th>Modal Price</th>
#                 </tr>
#             </thead>
#             <tbody>
#     """

#     for rec in records:
#         html += f"""
#         <tr>
#             <td>{rec.get('state', '')}</td>
#             <td>{rec.get('district', '')}</td>
#             <td>{rec.get('market', '')}</td>
#             <td>{rec.get('commodity', '')}</td>
#             <td>{rec.get('variety', '')}</td>
#             <td>{rec.get('grade', '')}</td>
#             <td>{rec.get('arrival_date', '')}</td>
#             <td>{rec.get('min_price', '')}</td>
#             <td>{rec.get('max_price', '')}</td>
#             <td>{rec.get('modal_price', '')}</td>
#         </tr>
#         """

#     html += """
#             </tbody>
#         </table>

#         <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
#         <script src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>
#         <script>
#             $(document).ready(function () {
#                 var table = $('#marketTable').DataTable();

#                 $('#stateFilter').on('change', function () {
#                     table.column(0).search(this.value).draw();
#                 });
#                 $('#districtFilter').on('change', function () {
#                     table.column(1).search(this.value).draw();
#                 });
#                 $('#commodityFilter').on('change', function () {
#                     table.column(3).search(this.value).draw();
#                 });
#             });
#         </script>
#     </body>
#     </html>
#     """

#     return html

@app.get("/table", response_class=HTMLResponse)
def get_table():
    records = fetch_all_data()

    # Extract unique values for filters
    states = sorted({rec.get('state', '') for rec in records if rec.get('state')})
    districts = sorted({rec.get('district', '') for rec in records if rec.get('district')})
    commodities = sorted({rec.get('commodity', '') for rec in records if rec.get('commodity')})

    html = """
    <html>
    <head>
        <title>Market Prices Table</title>
        <link rel="stylesheet" 
              href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css">
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, sans-serif;
                margin: 20px;
                background: linear-gradient(270deg, #fbc2eb, #a6c1ee, #ffd6a5, #fdffb6, #caffbf, #9bf6ff, #bdb2ff);
                background-size: 1400% 1400%;
                animation: gradientBG 20s ease infinite;
                color: #333;
            }
            @keyframes gradientBG {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
            h2 {
                text-align: center;
                color: #444;
                text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
            }
            select {
                margin-right: 10px;
                padding: 5px;
                border-radius: 8px;
                border: 1px solid #ccc;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                background: rgba(255,255,255,0.85);
                backdrop-filter: blur(4px);
            }
            table.dataTable {
                border-radius: 12px;
                overflow: hidden;
                background: rgba(255,255,255,0.9);
                box-shadow: 0 4px 20px rgba(0,0,0,0.15);
            }
            table.dataTable thead {
                background: linear-gradient(to right, #ff9a9e, #fad0c4, #fbc2eb, #a1c4fd, #c2e9fb);
                color: #333;
                font-weight: bold;
            }
            table.dataTable tbody tr:hover {
                background: rgba(255, 236, 210, 0.7);
                transition: background 0.3s ease;
            }
            label {
                font-weight: bold;
                color: #333;
            }
        </style>
    </head>
    <body>
        <h2>Market Prices</h2>

        <label>State: </label>
        <select id="stateFilter">
            <option value="">All</option>
    """
    for state in states:
        html += f"<option value='{state}'>{state}</option>"
    html += """
        </select>

        <label>District: </label>
        <select id="districtFilter">
            <option value="">All</option>
    """
    for dist in districts:
        html += f"<option value='{dist}'>{dist}</option>"
    html += """
        </select>

        <label>Commodity: </label>
        <select id="commodityFilter">
            <option value="">All</option>
    """
    for com in commodities:
        html += f"<option value='{com}'>{com}</option>"
    html += """
        </select>

        <table id="marketTable" class="display" style="width:100%">
            <thead>
                <tr>
                    <th>State</th>
                    <th>District</th>
                    <th>Market</th>
                    <th>Commodity</th>
                    <th>Variety</th>
                    <th>Grade</th>
                    <th>Arrival Date</th>
                    <th>Min Price</th>
                    <th>Max Price</th>
                    <th>Modal Price</th>
                </tr>
            </thead>
            <tbody>
    """

    for rec in records:
        html += f"""
        <tr>
            <td>{rec.get('state', '')}</td>
            <td>{rec.get('district', '')}</td>
            <td>{rec.get('market', '')}</td>
            <td>{rec.get('commodity', '')}</td>
            <td>{rec.get('variety', '')}</td>
            <td>{rec.get('grade', '')}</td>
            <td>{rec.get('arrival_date', '')}</td>
            <td>{rec.get('min_price', '')}</td>
            <td>{rec.get('max_price', '')}</td>
            <td>{rec.get('modal_price', '')}</td>
        </tr>
        """

    html += """
            </tbody>
        </table>

        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <script src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>
        <script>
            $(document).ready(function () {
                var table = $('#marketTable').DataTable();

                $('#stateFilter').on('change', function () {
                    table.column(0).search(this.value).draw();
                });
                $('#districtFilter').on('change', function () {
                    table.column(1).search(this.value).draw();
                });
                $('#commodityFilter').on('change', function () {
                    table.column(3).search(this.value).draw();
                });
            });
        </script>
    </body>
    </html>
    """

    return html


@app.get("/")
def root():
    return {"message": "Visit /raw for JSON data or /table for HTML table (with optional filters: state, district, market, commodity)"}


#npm install react react-dom
#npm install vite
#npm install -D tailwindcss postcss autoprefixer
#npx tailwindcss init -p
#npm install firebase 

#npm install 
#npm run dev