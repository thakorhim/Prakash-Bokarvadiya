import asyncio
from truecallerpy import search_phonenumber

# ✅ Step 1: यहां अपना Truecaller token पेस्ट करें
#token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."  # <== Paste your real token here

async def get_truecaller_details(phone_number, country_code):
    try:
        response = await search_phonenumber(phone_number, country_code)

        data = response.get("data")
        if data:
            print("📛 Name:", data.get("name", "N/A"))
            print("📍 City:", data.get("addresses")[0].get("city", "N/A") if data.get("addresses") else "N/A")
            print("📞 Number:", data.get("phones")[0].get("e164Format", "N/A") if data.get("phones") else "N/A")
            print("🟡 Carrier:", data.get("phones")[0].get("carrier", "N/A") if data.get("phones") else "N/A")
            print("👤 Gender:", data.get("gender", "N/A"))
            print("💼 Job Title:", data.get("jobTitle", "N/A"))
        else:
            print("❌ No data found or token is invalid.")
    except Exception as e:
        print("❌ Error:", e)

# Main function
if __name__ == "__main__":
    
    phone = input("📱 Enter phone number with country code (e.g. +917383471389): ")
    asyncio.run(get_truecaller_details(phone, "IN"))
