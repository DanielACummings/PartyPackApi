async function fetchPartyPack() {
    const btn = document.getElementById('refreshBtn');
    btn.disabled = true;
    btn.textContent = '⏳ Loading...';

    try {
        const response = await fetch('/api/party-pack');
        const data = await response.json();
        
        document.getElementById('partyPack').innerHTML = `
            <div class="item">
                <h3>😂 Joke</h3>
                <p>${data.joke}</p>
            </div>
            <div class="item">
                <h3>💡 Life Hack</h3>
                <p>${data.life_hack}</p>
            </div>
            <div class="item">
                <h3>🎪 Party Trick</h3>
                <p>${data.party_trick}</p>
            </div>
            <div class="item">
                <h3>😎 Pick Up Line</h3>
                <p>${data.pick_up_line}</p>
            </div>
        `;
    } catch (error) {
        document.getElementById('partyPack').innerHTML = `
            <div class="item" style="border-left-color: #ff6b6b;">
                <p>❌ Error loading party pack. Try again!</p>
            </div>
        `;
        console.error('Error:', error);
    } finally {
        btn.disabled = false;
        btn.textContent = '🔄 Get New Party Pack';
    }
}

// Load on page load
fetchPartyPack();
