// Key management for AES demo

const KEY_STORAGE = "aes_demo_key";

/**
 * Generate a random AES key of given length (16, 24, or 32)
 */
function generateKey(length = 16) {
    if (![16, 24, 32].includes(length)) length = 16;
    const array = new Uint8Array(length);
    window.crypto.getRandomValues(array);
    // Convert to hex string
    return Array.from(array, b => b.toString(16).padStart(2, '0')).join('').slice(0, length);
}

/**
 * Save key to localStorage
 */
function saveKey(key) {
    localStorage.setItem(KEY_STORAGE, key);
}

/**
 * Load key from localStorage
 */
function loadKey() {
    return localStorage.getItem(KEY_STORAGE) || "";
}

/**
 * Fill input field with saved key
 */
function applySavedKey() {
    const keyInput = document.getElementById("keyText");
    if (!keyInput) return;
    const savedKey = loadKey();
    if (savedKey) keyInput.value = savedKey;
}

/**
 * Generate new key and apply
 */
function generateAndApplyKey(length = 16) {
    const newKey = generateKey(length);
    saveKey(newKey);
    const keyInput = document.getElementById("keyText");
    if (keyInput) keyInput.value = newKey;
    return newKey;
}
