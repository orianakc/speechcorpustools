
from PyQt5 import QtGui, QtCore, QtWidgets

from ..helper import get_system_font_height

class HierarchyWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super(HierarchyWidget, self).__init__(parent)
        layout = QtWidgets.QVBoxLayout()
        self.hierarchy = None
        base_size =  get_system_font_height()
        self.hierarchyLayout = QtWidgets.QVBoxLayout()
        self.hierarchyLayout.setSpacing(0)
        self.hierarchyLayout.setStretch(0, 0)
        self.hierarchyLayout.setContentsMargins(0,0,0,0)
        self.hierarchyLayout.setAlignment(QtCore.Qt.AlignTop)
        self.spectrumLayout = QtWidgets.QVBoxLayout()
        self.spectrumLayout.setSpacing(0)
        self.spectrumLayout.setContentsMargins(0,0,0,0)
        s = QtWidgets.QLabel('Spectrogram')
        self.setFixedWidth(s.fontMetrics().width(s.text())*2)
        f = QtWidgets.QLabel('Formants')
        p = QtWidgets.QLabel('Pitch')
        v = QtWidgets.QLabel('Voicing')
        i = QtWidgets.QLabel('Intensity')
        s.setSizePolicy(QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Minimum)
        f.setSizePolicy(QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Minimum)
        p.setSizePolicy(QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Minimum)
        v.setSizePolicy(QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Minimum)
        i.setSizePolicy(QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Minimum)
        self.spectrumLayout.addWidget(s)
        #self.spectrumLayout.addWidget(f)
        #self.spectrumLayout.addWidget(p)
        #self.spectrumLayout.addWidget(v)
        #self.spectrumLayout.addWidget(i)
        self.hWidget = QtWidgets.QWidget()
        self.hWidget.setLayout(self.hierarchyLayout)

        layout.addWidget(self.hWidget)

        layout.addLayout(self.spectrumLayout)

        self.setLayout(layout)

    def resizeEvent(self, event):
        super(HierarchyWidget, self).resizeEvent(event)
        self.updateHierachy(self.hierarchy)

    def updateHierachy(self, hierarchy):
        if self.hierarchy is not None:
            while self.hierarchyLayout.count():
                item = self.hierarchyLayout.takeAt(0)
                if item.widget() is None:
                    continue
                item.widget().deleteLater()
        self.hierarchy = hierarchy
        if self.hierarchy is not None:
            space = (self.height() / 2) * 0.75
            half_space = space / 2
            per_type = half_space / len(self.hierarchy.keys())
            base_size =  get_system_font_height()
            spacing = (per_type - base_size) / 2
            self.hierarchyLayout.addSpacing(spacing * 2)
            for at in self.hierarchy.highest_to_lowest:
                w = QtWidgets.QLabel(at)
                w.setFixedWidth(w.fontMetrics().width(w.text()))
                w.setFixedHeight(base_size)
                w.setSizePolicy(QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Minimum)
                #w.clicked.connect(self.updateHierarchyVisibility)
                self.hierarchyLayout.addSpacing(spacing)
                self.hierarchyLayout.addWidget(w)
                self.hierarchyLayout.addSpacing(spacing)
            keys = []
            for k, v in sorted(self.hierarchy.subannotations.items()):
                for s in v:
                    keys.append((k,s))
            per_sub_type = half_space / len(keys)
            spacing = (per_sub_type - base_size) / 2
            for k in sorted(keys):
                w = QtWidgets.QLabel('{} - {}'.format(*k))
                w.setSizePolicy(QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Minimum)
                w.setFixedWidth(w.fontMetrics().width(w.text()))
                w.setFixedHeight(base_size)
                #w.clicked.connect(self.updateHierarchyVisibility)
                self.hierarchyLayout.addSpacing(spacing)
                self.hierarchyLayout.addWidget(w)
                self.hierarchyLayout.addSpacing(spacing)
