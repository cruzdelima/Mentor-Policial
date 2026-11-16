import Cocoa
import FlutterMacOS

class MainFlutterWindow: NSWindow {
  override func awakeFromNib() {
    let flutterViewController = FlutterViewController()
    self.contentViewController = flutterViewController

    // Janela inicial 1366 x 820, centralizada; tamanho mínimo 1180 x 720.
    let size = NSSize(width: 1366, height: 820)
    var frame = self.frame
    if let screen = NSScreen.main?.visibleFrame {
      frame.size = NSSize(width: min(size.width, screen.width), height: min(size.height, screen.height))
      frame.origin = NSPoint(x: screen.midX - frame.size.width / 2, y: screen.midY - frame.size.height / 2)
    }
    self.setFrame(frame, display: true)
    self.minSize = NSSize(width: 1180, height: 720)
    self.title = "Mentor Policial"

    RegisterGeneratedPlugins(registry: flutterViewController)

    super.awakeFromNib()
  }
}
