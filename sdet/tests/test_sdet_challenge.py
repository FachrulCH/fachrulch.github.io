"""
SDET Automation Challenge — Complete Solution
pytest + playwright (sync API)

Run:
    pip install pytest playwright
    playwright install chromium
    pytest tests/test_sdet_challenge.py -v
"""
import re

from playwright.sync_api import Page, expect


# ---------- Known data for lookups ----------

CAPITALS = {
    "France": "Paris",
    "Japan": "Tokyo",
    "Brazil": "Brasilia",
    "Australia": "Canberra",
    "Canada": "Ottawa",
    "Egypt": "Cairo",
    "Germany": "Berlin",
    "India": "New Delhi",
    "South Korea": "Seoul",
    "Turkey": "Ankara",
}

COLOR_CLASS_MAP = {
    "bg-crimson": "crimson",
    "bg-navy": "navy",
    "bg-forest": "forestgreen",
    "bg-gold": "gold",
    "bg-coral": "coral",
    "bg-slate": "slategray",
}

PROGRAMMING_LANGUAGES = {"Python", "JavaScript", "Rust", "Go", "TypeScript", "Java"}


# ---------- Helper ----------

def assert_solved(page: Page, challenge_num: int):
    """Assert that the challenge card has the 'solved' class."""
    card = page.locator(f"#challenge-{challenge_num}")
    expect(card).to_have_class(re.compile(r"solved"))


# ---------- Tests ----------


class TestChallenge01Dropdown:
    def test_select_correct_capital(self, page: Page):
        country = page.locator("#c1-country").inner_text()
        capital = CAPITALS[country]

        page.select_option("[data-testid='capital-select']", capital)
        page.locator("#challenge-1 .submit-btn").click()

        assert_solved(page, 1)


class TestChallenge02TextReversal:
    def test_reverse_text(self, page: Page):
        original = page.locator("#c2-original").inner_text()
        reversed_text = original[::-1]

        page.fill("[data-testid='reverse-input']", reversed_text)
        page.locator("#challenge-2 .submit-btn").click()

        assert_solved(page, 2)


class TestChallenge03CSSColorDetection:
    def test_detect_color_from_class(self, page: Page):
        class_hint = page.locator("#c3-class-hint").inner_text()
        # e.g. "CSS class: bg-crimson"
        css_class = class_hint.split(": ")[1].strip()
        color_name = COLOR_CLASS_MAP[css_class]

        page.fill("[data-testid='color-input']", color_name)
        page.locator("#challenge-3 .submit-btn").click()

        assert_solved(page, 3)


class TestChallenge04DragAndDrop:
    def test_drag_colors_to_zones(self, page: Page):
        for color in ["red", "blue", "green"]:
            source = page.locator(f"#drag-{color}")
            target = page.locator(f"#drop-{color}")
            source.drag_to(target)

        page.locator("#challenge-4 .submit-btn").click()

        assert_solved(page, 4)


class TestChallenge05DynamicCalculation:
    def test_sum_all_numbers(self, page: Page):
        number_elements = page.locator("#c5-numbers span")
        count = number_elements.count()
        total = sum(int(number_elements.nth(i).inner_text()) for i in range(count))

        page.fill("[data-testid='sum-input']", str(total))
        page.locator("#challenge-5 .submit-btn").click()

        assert_solved(page, 5)


class TestChallenge06ShadowDOM:
    def test_read_shadow_dom_secret(self, page: Page):
        # Playwright can pierce shadow DOM via >> notation or evaluate
        secret = page.evaluate("""
            () => document.getElementById('shadow-host')
                .shadowRoot.querySelector('.shadow-code').textContent
        """)

        page.fill("[data-testid='shadow-input']", secret)
        page.locator("#challenge-6 .submit-btn").click()

        assert_solved(page, 6)


class TestChallenge07HiddenElement:
    def test_find_hidden_token(self, page: Page):
        # The element is visually hidden but present in DOM
        token = page.locator("[data-testid='hidden-token']").inner_text()

        page.fill("[data-testid='hidden-input']", token)
        page.locator("#challenge-7 .submit-btn").click()

        assert_solved(page, 7)


class TestChallenge08DelayedElement:
    def test_wait_for_delayed_code(self, page: Page):
        # Wait up to 10s for the delayed element to become visible
        delayed = page.locator("[data-testid='delayed-code']")
        delayed.wait_for(state="visible", timeout=10_000)
        code = delayed.inner_text()

        page.fill("[data-testid='delayed-input']", code)
        page.locator("#challenge-8 .submit-btn").click()

        assert_solved(page, 8)


class TestChallenge09HoverToReveal:
    def test_hover_and_read_secret(self, page: Page):
        page.locator("[data-testid='hover-trigger']").hover()

        # After hover, the content is visible
        secret_word = page.locator("[data-testid='hover-secret']").inner_text()

        page.fill("[data-testid='hover-input']", secret_word)
        page.locator("#challenge-9 .submit-btn").click()

        assert_solved(page, 9)


class TestChallenge10TableDataExtraction:
    def test_find_top_scorer_email(self, page: Page):
        rows = page.locator("[data-testid='score-table'] tbody tr")
        row_count = rows.count()

        max_score = -1
        top_email = ""

        for i in range(row_count):
            cells = rows.nth(i).locator("td")
            email = cells.nth(1).inner_text()
            score = int(cells.nth(2).inner_text())
            if score > max_score:
                max_score = score
                top_email = email

        page.fill("[data-testid='table-input']", top_email)
        page.locator("#challenge-10 .submit-btn").click()

        assert_solved(page, 10)


class TestChallenge11IFrame:
    def test_read_iframe_value(self, page: Page):
        iframe = page.frame_locator("[data-testid='challenge-iframe']")
        value = iframe.locator("[data-testid='iframe-value']").inner_text()

        page.fill("[data-testid='iframe-input']", value)
        page.locator("#challenge-11 .submit-btn").click()

        assert_solved(page, 11)


class TestChallenge12EnableAndClick:
    def test_toggle_then_click(self, page: Page):
        submit_btn = page.locator("[data-testid='enabled-submit']")

        # Button should be disabled initially
        expect(submit_btn).to_be_disabled()

        # The checkbox is zero-size (opacity:0, width:0, height:0) behind a custom
        # toggle slider. Click the visible .toggle-slider sibling to toggle it.
        page.locator("#challenge-12 .toggle-slider").click()
        expect(submit_btn).to_be_enabled()

        submit_btn.click()

        assert_solved(page, 12)


class TestChallenge13DynamicAttributeSelector:
    def test_click_target_element(self, page: Page):
        target = page.locator('[data-target="true"]')
        target.click()

        assert_solved(page, 13)


class TestChallenge14MultiSelectCheckboxes:
    def test_select_only_programming_languages(self, page: Page):
        checkboxes = page.locator("#c14-checkboxes label")
        count = checkboxes.count()

        for i in range(count):
            label = checkboxes.nth(i)
            text = label.inner_text().strip()
            cb = label.locator("input[type='checkbox']")
            if text in PROGRAMMING_LANGUAGES:
                cb.check()
            else:
                cb.uncheck()

        page.locator("#challenge-14 .submit-btn").click()

        assert_solved(page, 14)


class TestChallenge15RightClickContextMenu:
    def test_right_click_reveal_code(self, page: Page):
        area = page.locator("[data-testid='context-area']")

        # Right-click to open context menu
        area.click(button="right")

        # Click "Reveal Code" option
        page.locator("[data-testid='reveal-code']").click()

        # Read the revealed code from the area
        revealed_text = area.inner_text()
        code = revealed_text.replace("Code: ", "").strip()

        page.fill("[data-testid='context-input']", code)
        page.locator("#challenge-15 .submit-btn").click()

        assert_solved(page, 15)


class TestChallenge16DoubleClick:
    def test_double_click_activation(self, page: Page):
        box = page.locator("[data-testid='dblclick-box']")
        box.dblclick()

        # Box should now show the code
        code = box.inner_text()

        page.fill("[data-testid='dblclick-input']", code)
        page.locator("#challenge-16 .submit-btn").click()

        assert_solved(page, 16)


class TestChallenge17SliderPrecision:
    def test_set_slider_to_target(self, page: Page):
        target = int(page.locator("[data-testid='slider-target']").inner_text())
        slider = page.locator("[data-testid='precision-slider']")

        # Set slider value via JavaScript for precision
        slider.evaluate(f"el => {{ el.value = {target}; el.dispatchEvent(new Event('input')); }}")

        page.locator("#challenge-17 .submit-btn").click()

        assert_solved(page, 17)


class TestChallenge18DialogHandling:
    def test_handle_alert_confirm_prompt(self, page: Page):
        # Read the expected prompt code from the page
        prompt_code = page.locator("#c18-prompt-code").inner_text()

        # Set up dialog handlers BEFORE triggering
        dialog_sequence = []

        def handle_dialog(dialog):
            dialog_sequence.append(dialog.type)
            if dialog.type == "alert":
                dialog.accept()
            elif dialog.type == "confirm":
                dialog.accept()
            elif dialog.type == "prompt":
                dialog.accept(prompt_code)

        page.on("dialog", handle_dialog)

        # Trigger the dialog sequence
        page.locator("[data-testid='dialog-trigger']").click()

        assert dialog_sequence == ["alert", "confirm", "prompt"]
        assert_solved(page, 18)


class TestChallenge19StaleElement:
    def test_capture_live_value(self, page: Page):
        # Read the current value and immediately submit
        # The element changes every 3 seconds, so we must be fast
        value = page.locator("[data-testid='stale-element']").inner_text()
        page.fill("[data-testid='stale-input']", value)
        page.locator("#challenge-19 .submit-btn").click()

        assert_solved(page, 19)


class TestChallenge20SortableList:
    def test_sort_list_ascending(self, page: Page):
        # Read all items and their values
        items = page.locator("[data-testid='sortable-list'] li")
        count = items.count()
        values = [int(items.nth(i).get_attribute("data-value")) for i in range(count)]
        sorted_values = sorted(values)

        # Use JavaScript to reorder the DOM (most reliable for sortable lists)
        page.evaluate("""
            () => {
                const list = document.getElementById('c20-list');
                const items = [...list.children];
                items.sort((a, b) => parseInt(a.dataset.value) - parseInt(b.dataset.value));
                items.forEach(item => list.appendChild(item));
            }
        """)

        page.locator("#challenge-20 .submit-btn").click()

        assert_solved(page, 20)


class TestFinalScore:
    """Run this last to verify all 20 challenges are solved in one session."""

    def test_all_challenges_solved(self, page: Page):
        """
        This test runs all challenges sequentially in one page session
        and verifies the final score is 20/20.
        """
        # --- Challenge 1: Dropdown ---
        country = page.locator("#c1-country").inner_text()
        page.select_option("[data-testid='capital-select']", CAPITALS[country])
        page.locator("#challenge-1 .submit-btn").click()

        # --- Challenge 2: Text Reversal ---
        original = page.locator("#c2-original").inner_text()
        page.fill("[data-testid='reverse-input']", original[::-1])
        page.locator("#challenge-2 .submit-btn").click()

        # --- Challenge 3: CSS Color ---
        css_class = page.locator("#c3-class-hint").inner_text().split(": ")[1].strip()
        page.fill("[data-testid='color-input']", COLOR_CLASS_MAP[css_class])
        page.locator("#challenge-3 .submit-btn").click()

        # --- Challenge 4: Drag & Drop ---
        for color in ["red", "blue", "green"]:
            page.locator(f"#drag-{color}").drag_to(page.locator(f"#drop-{color}"))
        page.locator("#challenge-4 .submit-btn").click()

        # --- Challenge 5: Sum Numbers ---
        nums = page.locator("#c5-numbers span")
        total = sum(int(nums.nth(i).inner_text()) for i in range(nums.count()))
        page.fill("[data-testid='sum-input']", str(total))
        page.locator("#challenge-5 .submit-btn").click()

        # --- Challenge 6: Shadow DOM ---
        secret = page.evaluate("""
            () => document.getElementById('shadow-host')
                .shadowRoot.querySelector('.shadow-code').textContent
        """)
        page.fill("[data-testid='shadow-input']", secret)
        page.locator("#challenge-6 .submit-btn").click()

        # --- Challenge 7: Hidden Element ---
        token = page.locator("[data-testid='hidden-token']").inner_text()
        page.fill("[data-testid='hidden-input']", token)
        page.locator("#challenge-7 .submit-btn").click()

        # --- Challenge 8: Wait for Delayed Element ---
        delayed = page.locator("[data-testid='delayed-code']")
        delayed.wait_for(state="visible", timeout=10_000)
        page.fill("[data-testid='delayed-input']", delayed.inner_text())
        page.locator("#challenge-8 .submit-btn").click()

        # --- Challenge 9: Hover ---
        page.locator("[data-testid='hover-trigger']").hover()
        word = page.locator("[data-testid='hover-secret']").inner_text()
        page.fill("[data-testid='hover-input']", word)
        page.locator("#challenge-9 .submit-btn").click()

        # --- Challenge 10: Table ---
        rows = page.locator("[data-testid='score-table'] tbody tr")
        max_score, top_email = -1, ""
        for i in range(rows.count()):
            cells = rows.nth(i).locator("td")
            email = cells.nth(1).inner_text()
            score = int(cells.nth(2).inner_text())
            if score > max_score:
                max_score, top_email = score, email
        page.fill("[data-testid='table-input']", top_email)
        page.locator("#challenge-10 .submit-btn").click()

        # --- Challenge 11: iFrame ---
        iframe = page.frame_locator("[data-testid='challenge-iframe']")
        value = iframe.locator("[data-testid='iframe-value']").inner_text()
        page.fill("[data-testid='iframe-input']", value)
        page.locator("#challenge-11 .submit-btn").click()

        # --- Challenge 12: Toggle & Click ---
        page.locator("#challenge-12 .toggle-slider").click()
        page.locator("[data-testid='enabled-submit']").click()

        # --- Challenge 13: Dynamic Attribute ---
        page.locator('[data-target="true"]').click()

        # --- Challenge 14: Multi-Select ---
        checkboxes = page.locator("#c14-checkboxes label")
        for i in range(checkboxes.count()):
            label = checkboxes.nth(i)
            cb = label.locator("input[type='checkbox']")
            if label.inner_text().strip() in PROGRAMMING_LANGUAGES:
                cb.check()
            else:
                cb.uncheck()
        page.locator("#challenge-14 .submit-btn").click()

        # --- Challenge 15: Right-Click ---
        page.locator("[data-testid='context-area']").click(button="right")
        page.locator("[data-testid='reveal-code']").click()
        code = page.locator("[data-testid='context-area']").inner_text()
        page.fill("[data-testid='context-input']", code.replace("Code: ", "").strip())
        page.locator("#challenge-15 .submit-btn").click()

        # --- Challenge 16: Double Click ---
        box = page.locator("[data-testid='dblclick-box']")
        box.dblclick()
        page.fill("[data-testid='dblclick-input']", box.inner_text())
        page.locator("#challenge-16 .submit-btn").click()

        # --- Challenge 17: Slider ---
        target = page.locator("[data-testid='slider-target']").inner_text()
        page.locator("[data-testid='precision-slider']").evaluate(
            f"el => {{ el.value = {target}; el.dispatchEvent(new Event('input')); }}"
        )
        page.locator("#challenge-17 .submit-btn").click()

        # --- Challenge 18: Dialogs ---
        prompt_code = page.locator("#c18-prompt-code").inner_text()

        def handle_dialog(dialog):
            if dialog.type == "prompt":
                dialog.accept(prompt_code)
            else:
                dialog.accept()

        page.on("dialog", handle_dialog)
        page.locator("[data-testid='dialog-trigger']").click()

        # --- Challenge 19: Stale Element ---
        val = page.locator("[data-testid='stale-element']").inner_text()
        page.fill("[data-testid='stale-input']", val)
        page.locator("#challenge-19 .submit-btn").click()

        # --- Challenge 20: Sort List ---
        page.evaluate("""
            () => {
                const list = document.getElementById('c20-list');
                const items = [...list.children];
                items.sort((a, b) => parseInt(a.dataset.value) - parseInt(b.dataset.value));
                items.forEach(item => list.appendChild(item));
            }
        """)
        page.locator("#challenge-20 .submit-btn").click()

        # --- Verify final score ---
        score = page.locator("#score-display")
        expect(score).to_have_text("Score: 20 / 20")
