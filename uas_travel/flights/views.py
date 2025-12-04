from django.shortcuts import render
from .services import search_flight_offers

def parse_flight_data(flight_raw):
    try:
        itineraries = flight_raw.get('itineraries', [])
        if not itineraries: return None
            
        itinerary = itineraries[0] 
        segments = itinerary.get('segments', [])
        if not segments: return None
            
        first_segment = segments[0]
        last_segment = segments[-1]  
        
        raw_duration = itinerary.get('duration', '')
        duration = raw_duration.replace('PT', '').replace('H', 'h ').replace('M', 'm').lower()

        price_dict = flight_raw.get('price', {})
        price = price_dict.get('total', '0')
        currency = price_dict.get('currency', 'EUR')

        return {
            'id': flight_raw.get('id'),
            'carrier': first_segment.get('carrierCode', '??'),
            'flight_number': first_segment.get('number', '0000'),
            
            'departure': first_segment.get('departure', {}).get('iataCode'),
            'arrival': last_segment.get('arrival', {}).get('iataCode'),
            
            'dep_time': first_segment.get('departure', {}).get('at', '').replace('T', ' '),
            'duration': duration,
            'price': f"{currency} {price}",
            'price_raw': price
        }
    except Exception as e:
        print(f"⚠️ PARSING ERROR: {e}")
        return None

def index(request):
    return render(request, 'index.html')

def flight_result(request):
    origin = request.GET.get('origin')
    destination = request.GET.get('destination')
    date = request.GET.get('date')
    return_date = request.GET.get('return_date')

    print(f"--- SEARCHING: {origin} to {destination} on {date} ---")

    raw_data = search_flight_offers(origin, destination, date, return_date)
    
    flights = []
    if raw_data:
        print(f"✅ API SUCCESS: Ditemukan {len(raw_data)} data mentah.")
        for f in raw_data:
            parsed = parse_flight_data(f)
            if parsed: 
                flights.append(parsed)
            else:
                print("❌ Gagal parsing salah satu data penerbangan.")
    else:
        print("⚠️ API WARNING: Tidak ada data yang dikembalikan dari Amadeus (raw_data is None/Empty).")

    context = {
        'flights': flights,
        'origin': origin,
        'destination': destination,
        'date': date,
        'return_date': return_date
    }
    return render(request, 'result.html', context)

def flight_booking(request):
    context = {
        'price': request.GET.get('price'),
        'carrier': request.GET.get('carrier'),
        'number': request.GET.get('number'),
        'origin': request.GET.get('origin'),
        'destination': request.GET.get('destination'),
        'dep_time': request.GET.get('dep_time'),
        'duration': request.GET.get('duration'),
        'return_date': request.GET.get('return_date'),
    }
    return render(request, 'booking.html', context)