import { defineConfig } from 'vite'
import { resolve } from 'path'
import { readdirSync } from 'fs'
import { fileURLToPath } from 'url'

const __dirname = fileURLToPath(new URL('.', import.meta.url))

// Collect all component pages
const componentPages = Object.fromEntries(
  readdirSync(resolve(__dirname, 'components'))
    .filter(f => f.endsWith('.html'))
    .map(f => [
      `comp-${f.replace('.html', '')}`,
      resolve(__dirname, 'components', f)
    ])
)

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main:  resolve(__dirname, 'index.html'),
        icons: resolve(__dirname, 'icons.html'),
        demo:  resolve(__dirname, 'demo.html'),
        ...componentPages  // 48 component pages
      }
    }
  }
})
