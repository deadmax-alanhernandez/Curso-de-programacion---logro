<?php
for ($it = 1; $it <= 30; $it++) {
    if ($it % 3 == 0 && $it % 5 == 0) {
        echo "MarTierra\n";
    } elseif ($it % 3 == 0) {
        echo "Mar\n";
    } elseif ($it % 5 == 0) {
        echo "Tierra\n";
    } else {
        echo "$it\n";
    }
}
?>