from PySide6.QtGui import QFont, Qt, QPen, QColor, QBrush


class Settings:
    BLOCK_SIZE = 10

    _TRANSPARENT_COLOR = Qt.transparent
    _SELECTION_COLOR = QColor(254, 95, 0)

    _ELEMENT_NORMAL_COLOR = Qt.black
    _ELEMENT_SELECTED_COLOR = QColor(0, 159, 183)
    _ELEMENT_SHAPE_SELECTED_COLOR = _SELECTION_COLOR
    _LINE_SELECTED_COLOR = _SELECTION_COLOR

    _HANDLE_NORMAL_COLOR = _ELEMENT_SELECTED_COLOR
    _HANDLE_SELECTED_COLOR = _SELECTION_COLOR

    _ELEMENT_NORMAL_BRUSH_COLOR = _ELEMENT_NORMAL_COLOR
    _ELEMENT_SELECTED_BRUSH_COLOR = _ELEMENT_SELECTED_COLOR
    _ELEMENT_NORMAL_TRANSPARENT_BRUSH_COLOR = _TRANSPARENT_COLOR
    _ELEMENT_SELECTED_TRANSPARENT_BRUSH_COLOR = _TRANSPARENT_COLOR

    _HANDLE_PEN_SIZE = 2
    HANDLE_NORMAL_PEN = QPen(_HANDLE_NORMAL_COLOR, _HANDLE_PEN_SIZE)
    HANDLE_SELECTED_PEN = QPen(_HANDLE_SELECTED_COLOR, _HANDLE_PEN_SIZE)

    ELEMENT_PEN_SIZE = 2
    ELEMENT_SHAPE_SIZE = 4
    ELEMENT_NORMAL_PEN = QPen(_ELEMENT_NORMAL_COLOR, ELEMENT_PEN_SIZE, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
    ELEMENT_SELECTED_PEN = QPen(_ELEMENT_SELECTED_COLOR, ELEMENT_PEN_SIZE, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
    ELEMENT_SHAPE_SELECTED_PEN = QPen(_ELEMENT_SHAPE_SELECTED_COLOR, ELEMENT_SHAPE_SIZE, Qt.DotLine, Qt.RoundCap, Qt.RoundJoin)

    LINE_SELECTED_PEN = QPen(_LINE_SELECTED_COLOR, ELEMENT_PEN_SIZE, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)

    ELEMENT_NORMAL_BRUSH = QBrush(_ELEMENT_NORMAL_BRUSH_COLOR)
    ELEMENT_SELECTED_BRUSH = QBrush(_ELEMENT_SELECTED_BRUSH_COLOR)
    ELEMENT_NORMAL_TRANSPARENT_BRUSH = QBrush(_ELEMENT_NORMAL_TRANSPARENT_BRUSH_COLOR)
    ELEMENT_SELECTED_TRANSPARENT_BRUSH = QBrush(_ELEMENT_SELECTED_TRANSPARENT_BRUSH_COLOR)

    LINE_SELECTED_BRUSH = QBrush(_LINE_SELECTED_COLOR)

    ELEMENT_TEXT_NORMAL_COLOR = Qt.black
    ELEMENT_TEXT_SELECTED_COLOR = _ELEMENT_SELECTED_COLOR

    ELEMENT_TEXT_NORMAL_PEN = QPen(ELEMENT_TEXT_NORMAL_COLOR)
    ELEMENT_TEXT_SELECTED_PEN = QPen(ELEMENT_TEXT_SELECTED_COLOR)

    _GRID_COLOR = QColor(191, 215, 181)
    GRID_PEN = QPen(_GRID_COLOR, 0.5, Qt.SolidLine)

    ELEMENT_PADDING = 0

    ACTOR_BASE_SIZE = 5
    ELLIPSE_SCALE_WIDTH = 1.33
    ELLIPSE_SCALE_HEIGHT = 1.33
    CLASS_MIN_COMPARTMENT_HEIGHT = 10
    PACKAGE_DELTA_WIDTH1 = 20
    PACKAGE_EMPTY_HEIGHT1 = 15
    NOTE_DELTA = 15
    LINE_HANDLE_SIZE = 15
    LINE_HALF_WIDTH = 10

    element_font = QFont('Monospace', 10)
    element_font.setStyleHint(QFont.TypeWriter)
