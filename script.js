let allSongs = [];
let showChorusSongs = false; // New state variable

window.addEventListener('DOMContentLoaded', () => {
    fetch('./songs.json')
        .then(res => {
            if (!res.ok) throw new Error('Could not load songs.json');
            return res.json();
        })
        .then(data => {
            allSongs = data.songs;
            displaySongs(allSongs);
        })
        .catch(err => {
            console.error('Error loading songs:', err);
            document.getElementById('songList').innerHTML = `<p style="color: #b0005a;">⚠️ Failed to load <code>songs.json</code>.</p>`;
        });

    document.getElementById('nameFilter').addEventListener('input', applyFilters);
    document.getElementById('singerFilter').addEventListener('input', applyFilters);
    document.getElementById('tagFilter').addEventListener('input', applyFilters);

    const chorusButton = document.getElementById('chorusFilterBtn');
    chorusButton.addEventListener('click', () => {
        showChorusSongs = !showChorusSongs; // Toggle the state
        chorusButton.textContent = showChorusSongs ? 'Show All Songs' : 'Show Chorus Songs';
        applyFilters(); // Reapply filters
    });

    const removeAllFiltersBtn = document.getElementById('removeAllFiltersBtn');
    removeAllFiltersBtn.addEventListener('click', removeAllFilters);
});

function removeAllFilters() {
    document.getElementById('nameFilter').value = '';
    document.getElementById('singerFilter').value = '';
    document.getElementById('tagFilter').value = '';
    showChorusSongs = false;
    document.getElementById('chorusFilterBtn').textContent = 'Show Chorus Songs';
    applyFilters();
}

function applyFilters() {
    const nameInput = document.getElementById('nameFilter').value.trim().toLowerCase();
    const singerInput = document.getElementById('singerFilter').value.trim().toLowerCase();
    const tagInput = document.getElementById('tagFilter').value.trim().toLowerCase();

    const filtered = allSongs.filter(song => {
        const singers = Array.isArray(song.singers) ? song.singers : [song.singers];
        const rawTags = song.tags;
        const tags = Array.isArray(rawTags) ? rawTags : (typeof rawTags === 'string' ? [rawTags] : []);

        const nameMatch = !nameInput || song.name.toLowerCase().includes(nameInput);
        const singerMatch = !singerInput || singers.some(s => s.toLowerCase().includes(singerInput));
        const tagMatch = !tagInput || tags.some(t => t.toLowerCase().includes(tagInput));

        // New chorus filter logic
        const chorusMatch = !showChorusSongs || singers.length > 1;

        return nameMatch && singerMatch && tagMatch && chorusMatch;
    });

    displaySongs(filtered);
}

function displaySongs(songs) {
    const container = document.getElementById('songList');
    container.innerHTML = '';

    // Create and update the song count display
    let songCountDisplay = document.getElementById('songCount');
    if (!songCountDisplay) {
        songCountDisplay = document.createElement('p');
        songCountDisplay.id = 'songCount';
        // Insert it right after the filters div
        document.querySelector('.filters').insertAdjacentElement('afterend', songCountDisplay);
    }
    songCountDisplay.innerHTML = `Showing <b>${songs.length}</b> of <b>${allSongs.length}</b> songs.`;


    if (songs.length === 0) {
        container.innerHTML = '<p>No songs found matching your criteria.</p>';
        return;
    }

    songs.forEach(song => {
        const songDiv = document.createElement('div');
        songDiv.className = 'song';

        const name = document.createElement('h2');
        name.textContent = song.name;
        songDiv.appendChild(name);

        // Singers row
        const singersRow = document.createElement('div');
        singersRow.className = 'meta-row';

        const singersLabel = document.createElement('div');
        singersLabel.className = 'meta-label';
        singersLabel.textContent = 'Singers:';
        singersRow.appendChild(singersLabel);

        const singers = Array.isArray(song.singers) ? song.singers : [song.singers];
        singers.forEach(singer => {
            const singerSpan = document.createElement('span');
            singerSpan.className = 'singer';
            singerSpan.textContent = singer;
            singersRow.appendChild(singerSpan);
        });

        // Tags row
        const tagsRow = document.createElement('div');
        tagsRow.className = 'meta-row';

        const tagsLabel = document.createElement('div');
        tagsLabel.className = 'meta-label';
        tagsLabel.textContent = 'Tags:';
        tagsRow.appendChild(tagsLabel);

        // Normalize tags into an array
        const rawTags = song.tags;
        const tags = Array.isArray(rawTags) ? rawTags : (typeof rawTags === 'string' ? [rawTags] : []);

        tags.forEach(tag => {
            const tagSpan = document.createElement('span');
            tagSpan.className = 'tag';
            tagSpan.textContent = tag;
            tagsRow.appendChild(tagSpan);
        });

        songDiv.appendChild(singersRow);
        songDiv.appendChild(tagsRow);
        container.appendChild(songDiv);
    });
}